import os
import numpy as np
import pandas as pd
import pyqtgraph as pg

from collections import deque
from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox,
    QVBoxLayout, QFileDialog,
    QTableWidgetItem,
)

current_dir = os.path.dirname(os.path.abspath(__file__))
if os.name == 'nt':
    os.add_dll_directory(current_dir)
import ftd2xx as ftd


pg.setConfigOptions(antialias=True)

CCD_PIXELS = 3648  # pixel number
PIXEL_SIZE = 0.008  # mm
LAMBDA = 632.8e-6  # lambda (mm)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # FT handle
        self.ft_handle = None

        self.isRead = False
        self.isFT245 = False
        self.isRecord = False

        # Data cache queue, retaining the latest 10 measurement results
        self.D = deque(maxlen=10)

        # Automatic Measurement Timer
        self.calcTimer = QTimer(self)
        self.calcTimer.timeout.connect(self.updateMeasure)

        self.ccdTimer = QTimer(self)
        self.ccdTimer.timeout.connect(self.readCCD)

        self.intervalBox.clear()
        self.intervalBox.addItems(['1', '10', '30'])
        self.intervalBox.currentTextChanged.connect(self.updateTimer)

        self.plotter = pg.PlotWidget(background='w')  # white background
        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.plotter)

        self.plotter.setLabel('bottom', "Pixel")
        self.plotter.setLabel('left', "Gray Value")
        self.plotter.setYRange(0, 65535, padding=0)
        self.plotter.setXRange(0, CCD_PIXELS, padding=0)
        self.plotter.showGrid(x=True, y=True, alpha=0.3)
        self.plotter.setMouseEnabled(x=False, y=False)
        
        self.curve = self.plotter.plot(pen=pg.mkPen('k', width=2))

        self.refreshBtn.clicked.connect(self.refreshPort)
        self.openBtn.clicked.connect(self.setFT245)
        self.setBtn.clicked.connect(self.setIntTime)
        self.readBtn.clicked.connect(self.setTimer)
        self.recordBtn.clicked.connect(self.recordData)
        self.saveBtn.clicked.connect(self.saveData)
        self.deleteBtn.clicked.connect(self.deleteData)
        self.clearBtn.clicked.connect(self.clearData)

        self.refreshPort()


    @Slot()
    def recordData(self):
        if not self.isRead:
            QMessageBox.critical(
                self,
                "Record Error",
                "There is no data read!"
            )
            return
        if self.isRecord:
            self.isRecord = False
            self.recordBtn.setText("Record")
        else:
            self.isRecord = True
            self.recordBtn.setText("Not Record")


    @Slot()
    def saveData(self):
        total_rows = self.tableWidget.rowCount()
        if total_rows == 0:
            self.textBrowser.append(
                "> <span style='color: red'>Data save failed</span>\n"
            )
            QMessageBox.critical(
                self,
                "Save Error",
                "There is no recorded data in the table!"
            )
            return
        
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Recorded Data",
            "results/",  # default path
            "Excel Files (*.xlsx);;All Files (*)"
        )
        if not file_path:
            return
        
        headers = []
        total_cols = self.tableWidget.columnCount()
        for col in range(total_cols):
            header_item = self.tableWidget.horizontalHeaderItem(col)
            headers.append(header_item.text() if header_item else f"Column {col+1}")

        all_data = []
        for row in range(total_rows):
            row_data = []
            for col in range(total_cols):
                cell_item = self.tableWidget.item(row, col)
                row_data.append(cell_item.text() if cell_item else "")
            all_data.append(row_data)
        
        try:
            df = pd.DataFrame(all_data, columns=headers)
            df.to_excel(file_path, index=False, engine="openpyxl")
            self.textBrowser.append(
                f"> <span style='color:green'>Data has been saved to:\n{file_path}</span>"
            )
        except Exception as e:
            self.textBrowser.append(
                f"> <span style='color: red'>Failed to save file:\n{str(e)}</span>\n"
            )
            QMessageBox.critical(
                self,
                "Save Failed",
                f"Failed to save file:\n{str(e)}"
            )


    @Slot()
    def deleteData(self):
        current_row = self.tableWidget.currentRow()
        if current_row == -1:
            return
        
        self.tableWidget.removeRow(current_row)


    @Slot()
    def clearData(self):
        self.tableWidget.setRowCount(0)


    def closeEvent(self, event):  # re-write close event
        self.calcTimer.stop()
        if self.ft_handle is not None:
            try:
                self.ft_handle.close()
            except:
                pass
        super().closeEvent(event)


    @Slot()
    def refreshPort(self):
        if not self.isFT245 and not self.isRead:
            self.portBox.clear()
            dev_list = ftd.listDevices()
            if dev_list:
                for dev in dev_list:
                    self.portBox.addItem(dev.decode('utf-8', errors='ignore'))
            else:
                self.portBox.addItem("No Devices")
        else:
            QMessageBox.warning(self, "Warning", "Please close port first!")


    @Slot()
    def setFT245(self):
        if self.isFT245:
            self.isFT245 = False
            self.openBtn.setText("Open Device")
            if self.ft_handle is not None:
                try:
                    self.ft_handle.close()
                except:
                    pass
                self.ft_handle = None
                self.textBrowser.append(
                    "> <span style='color: green'>Device closed</span>\n"
                )
        else:
            try:
                if not ftd.listDevices():
                    self.textBrowser.append(
                        "> <span style='color: red'>No device be found</span>\n"
                    )
                    QMessageBox.warning(self, "Warning", "No device be found!")
                    return
                
                self.ft_handle = ftd.open(0)
                self.ft_handle.resetDevice()
                self.ft_handle.purge(ftd.defines.PURGE_RX | ftd.defines.PURGE_TX)
                self.ft_handle.setTimeouts(1000, 1000)

                self.isFT245 = True
                self.openBtn.setText("Close Device")
                self.textBrowser.append(
                    "> <span style='color: green'>Device opened successfully</span>\n"
                )
            except Exception as e:
                self.textBrowser.append(
                    f"> <span style='color: red'>Failed to open device: {e}</span>\n"
                )
                QMessageBox.warning(self, "Error", f"Failed to open device: {e}")


    @Slot()
    def setIntTime(self):
        if not self.isFT245:
            self.textBrowser.append(
                "> <span style='color: red'>Device not enabled</span>\n"
            )
            QMessageBox.warning(
                self, "Error", "Device FT245RL not enabled!"
            )
        else:
            time = int(self.timeBox.value())
            cmd = f"#CCDInt:{time:03d}%"
            self.ft_handle.write(cmd.encode('utf-8'))
            self.textBrowser.append(
                f"> <span style='color: green'>Integral time command sent: {time} ms</span>\n"
            )


    @Slot()
    def setTimer(self):
        if self.isRead:
            self.isRead = False
            self.ccdTimer.stop()
            self.calcTimer.stop()
            self.clearPlotter()
            self.readBtn.setText("Read CCD")
            self.textBrowser.append(
                "> <span style='color: green'>Auto reading stopped</span>\n"
            )
        else:
            if self.isFT245:
                self.isRead = True
                self.D.clear()
                self.readBtn.setText("Close CCD")
                self.readCCD()
                self.calcTimer.start(
                    int(self.intervalBox.currentText()) * 1000
                )  # ms
                self.ccdTimer.start(150)  # 150ms
            else:
                self.textBrowser.append(
                    "> <span style='color: red'>Device not enabled</span>\n"
                )
                QMessageBox.warning(
                    self, "Error", "Device FT245RL not enabled!"
                )


    @Slot()
    def updateTimer(self):
        if self.isRead:
            self.D.clear()
            self.calcTimer.start(int(self.intervalBox.currentText())*1000)


    @Slot()
    def readCCD(self):
        if not self.isFT245 or self.ft_handle is None:
            return
        try:
            self.ft_handle.write(b"#?data%")

            # read pixel data (3648 * 2 = 7296 byte)
            bytes_to_read = CCD_PIXELS * 2
            ccd_raw = self.ft_handle.read(bytes_to_read)
            
            if len(ccd_raw) != bytes_to_read:
                self.textBrowser.append(
                    f"> <span style='color: red'>Data length error, received {len(ccd_raw)} bytes</span>\n"
                )
                return
            
            ccd_data = np.frombuffer(ccd_raw, dtype='>u2').astype(np.float64)
            filtered_data = self.smoothData(ccd_data, window=80)  # changable
            self.deltaX = self.calcDeltaX(filtered_data)
            if self.deltaX > 0:
                self.xEdit.setText(str(self.deltaX))
            else:
                self.xEdit.setText("0")
            self.plotCCD(filtered_data, cross_points=None)
        except Exception as e:
            self.textBrowser.append(
                f"> <span style='color: red'>Read Error: {e}</span>\n"
            )
            if "FT_INVALID_HANDLE" in str(e) or "FT_IO_ERROR" in str(e):
                self.setTimer()


    @Slot()
    def updateMeasure(self):
        if not self.isFT245 or self.ft_handle is None:
            return
        try:
            d = self.calcD(self.deltaX)
            if d > 0:
                self.D.append(d)
                self.calcStatistics()
                if self.isRecord:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(f"{d:.2f}"))
        except Exception as e:
            self.textBrowser.append(
                f"> <span style='color: red'>Read Error: {e}</span>\n"
            )
            if "FT_INVALID_HANDLE" in str(e) or "FT_IO_ERROR" in str(e):
                self.setTimer()


    def calcStatistics(self):
        if len(self.D) == 0:
            return
        mean = np.mean(self.D)
        rms = np.std(self.D)
        
        self.meanEdit.setText(f"{mean:.4f}")
        self.RMSEdit.setText(f"{rms:.4f}")


    def smoothData(
        self, 
        data: np.ndarray, 
        window: int
    ) -> np.ndarray:
        kernel = np.ones(window) / window
        return np.convolve(data, kernel, mode='same')


    def calcDeltaX(self, data: np.ndarray) -> int:
        threshold = int(self.thrEdit.text().strip())
        min = self.findLocalMin(data, threshold)
        
        if len(min) < 2:
            return -1  # can't calculate delta x
        
        x1, x2 = min[0], min[1]
        self.x1Edit.setText(str(x1))
        self.x2Edit.setText(str(x2))
        
        return x2 - x1


    def findLocalMin(
        self, 
        data: np.ndarray, 
        threshold: float
    ) -> list:
        min = []  # local min index

        i = 2401  # begin index
        while i < 3200 and i < len(data) - 1:
            if (data[i] < data[i-1] and 
                data[i] < data[i+1] and 
                data[i] < threshold):
                min.append(i)
                i += 300  # need 
            else:
                i += 1
        
        min.sort()  # from small to big (index)
        if len(min) > 2:
            min = min[:2]  # first two index
        
        return min


    def calcD(self, deltaX: int):
        if deltaX <= 0:
            self.DEdit.setText("0.00")
            return -1.0
        L = float(self.LEdit.text().strip())

        X = deltaX * PIXEL_SIZE  # (mm)
        if X == 0:  # zero test
            self.DEdit.setText("0.00")
            return -1.0
        D = (LAMBDA * L) / X  # (mm)
        
        self.DEdit.setText(f"{D:.4f}")
        return D


    def plotCCD(
        self,
        data,
        cross_points  # guide line
    ):
        x = np.arange(len(data))
        self.curve.setData(x, data)
        
        for item in list(self.plotter.items()):
            if isinstance(item, (pg.InfiniteLine, pg.TextItem)):
                self.plotter.removeItem(item)
        
        if cross_points is None:
            return

        for pos in cross_points:
            line = pg.InfiniteLine(
                pos=pos, angle=90,
                pen=pg.mkPen('b', width=2, style=Qt.DashLine)
            )
            self.plotter.addItem(line)


    def clearPlotter(self):
        self.curve.setData([], [])
        
        for item in list(self.plotter.items()):
            if isinstance(item, (pg.InfiniteLine, pg.TextItem)):
                self.plotter.removeItem(item)
        
        self.xEdit.setText("0")
        self.x1Edit.setText("0")
        self.x2Edit.setText("0")
        self.DEdit.setText("0.0000")
        self.meanEdit.setText("0.0000")
        self.RMSEdit.setText("0.0000")
