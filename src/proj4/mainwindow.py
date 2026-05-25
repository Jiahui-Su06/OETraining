import os
import math
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
N = 1.5163  # refractive index
ALPHA = math.radians(4)  # radian

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # FT handle
        self.ft_handle = None
        self.h1, self.h2 = -1, -1

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
            return
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
            self.h1, self.h2, cross_points = self.calcH1H2(filtered_data)

            self.H1Edit.setText(str(self.h1) if self.h1 != -1 else "0")
            self.H2Edit.setText(str(self.h2) if self.h2 != -1 else "0")
            
            self.plotCCD(filtered_data, cross_points)
        except Exception as e:
            self.textBrowser.append(
                f"> <span style='color: red'>Read Error: {e}</span>\n"
            )
            if "FT_INVALID_HANDLE" in str(e) or "FT_IO_ERROR" in str(e):
                self.setTimer()


    def updateMeasure(self):
        if not self.isFT245 or self.ft_handle is None:
            return
        try:
            d = self.calcD(self.h1, self.h2)
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
        self.RMSEdit.setText(f"{rms:.6f}")


    def smoothData(self, data, window=7):
        kernel = np.ones(window) / window
        return np.convolve(data, kernel, mode='same')


    def calcH1H2(self, data):
        skip = 200
        n_len = len(data)
        if n_len <= 2 * skip:
            return -1, -1, None
            
        sub_data = data[skip : n_len - skip]
        
        # calculate threshold value
        min_val = np.min(sub_data)
        max_val = np.max(sub_data)
        threshold = min_val + (max_val - min_val) * 0.5
        
        # detect threshold
        cross_points = []
        for i in range(1, len(sub_data)):
            if (sub_data[i-1] < threshold <= sub_data[i]) or \
               (sub_data[i-1] > threshold >= sub_data[i]):
                cross_points.append(i + skip)

        # select 2, 3, 4 points
        if len(cross_points) >= 4:
            a = cross_points[1]   # when it is in 0, 1, 2, the result is true
            b = cross_points[2]
            c = cross_points[3]
            h1 = b - a
            h2 = c - a
            return h1, h2, cross_points[1:4]   # TODO:this place need to change
        else:
            return -1, -1, None


    def calcD(self, h1, h2):
        if h1 <= 0 or h2 <= 0:
            self.DEdit.setText("0.0000")
            return -1.0
        
        L1 = float(self.L1Edit.text().strip())
        
        H1 = h1 * PIXEL_SIZE
        H2 = h2 * PIXEL_SIZE
        
        denominator = 2 * ALPHA * L1 * (N-1) + H2
        if denominator == 0:
            self.DEdit.setText("0.0000")
            return -1.0
        
        d = 2*ALPHA*L1*H1*(N-1) / denominator
        self.DEdit.setText(f"{d:.4f}")
        return d


    def plotCCD(self, data, cross_points):
        x = np.arange(len(data))
        self.curve.setData(x, data)
        
        for item in list(self.plotter.items()):
            if isinstance(item, (pg.InfiniteLine, pg.TextItem)):
                self.plotter.removeItem(item)
        
        if cross_points is None:
            return
        
        colors = ['r', 'g', 'b']
        labels = ['P1', 'P2', 'P3']

        for i, pos in enumerate(cross_points):
            line = pg.InfiniteLine(
                pos=pos, angle=90,
                pen=pg.mkPen(colors[i], width=2, style=Qt.DashLine)
            )
            self.plotter.addItem(line)
            # add label
            label = pg.TextItem(labels[i], color=colors[i], anchor=(0, 1))
            label.setPos(pos, np.max(data) if len(data)>0 else 60000)
            self.plotter.addItem(label)


    def clearPlotter(self):
        self.curve.setData([], [])
        
        for item in list(self.plotter.items()):
            if isinstance(item, (pg.InfiniteLine, pg.TextItem)):
                self.plotter.removeItem(item)
        
        self.H1Edit.setText("0")
        self.H2Edit.setText("0")
        self.DEdit.setText("0.0000")
