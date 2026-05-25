import numpy as np
import pandas as pd

from plotdialog import PlotDialog
from ui_mainwindow import Ui_MainWindow

from PySide6.QtCore import Qt, QTimer, QIODevice, Slot
from PySide6.QtGui import QPen, QPainter
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import (
    QMainWindow, QMessageBox, QGraphicsScene,
    QTableWidgetItem, QFileDialog,
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.textBrowser.append("> <span style='color: blue'>Initializing...</span>\n")
        self.graphics_items = []

        # add target scene
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setRenderHints(QPainter.Antialiasing)

        # set serial port
        self.serialPort = QSerialPort(self)
        self.requestTimer = QTimer(self)
        self.buffer = bytes()

        self.serialPort.setBaudRate(QSerialPort.BaudRate.Baud115200)
        self.serialPort.setDataBits(QSerialPort.DataBits.Data8)
        self.serialPort.setParity(QSerialPort.Parity.NoParity)
        self.serialPort.setStopBits(QSerialPort.StopBits.OneStop)
        self.serialPort.setFlowControl(QSerialPort.FlowControl.NoFlowControl)

        # set port combobox items
        for info in QSerialPortInfo.availablePorts():
            self.portComboBox.addItem(info.portName())

        self.connectBtn.clicked.connect(self.setSerialPort)
        self.setResistanceBtn.clicked.connect(self.setResistance)
        self.recordBtn.clicked.connect(self.recordData)
        self.deleteBtn.clicked.connect(self.deleteData)
        self.clearBtn.clicked.connect(self.clearData)
        self.saveBtn.clicked.connect(self.saveData)

        self.actionSave.triggered.connect(self.saveData)
        self.actionOpen.triggered.connect(self.openData)
        self.actionQuit.triggered.connect(self.close)
        self.actionClose.triggered.connect(self.deleteData)
        self.actionRecord.triggered.connect(self.recordData)
        self.actionDelete.triggered.connect(self.deleteData)
        self.actionClear.triggered.connect(self.clearData)
        self.actionHelp.triggered.connect(self.showHelp)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionAnalysis.triggered.connect(self.analysisData)

        self.serialPort.readyRead.connect(self.readData)
        self.requestTimer.timeout.connect(self.requestData)
        self.serialPort.errorOccurred.connect(self.handleError)

        self.X = 50.0
        self.Y = 50.0
        self.pxEdit.setText(f"{self.X}")
        self.pyEdit.setText(f"{self.Y}")
        self.v00Edit.setText("0")
        self.v01Edit.setText("0")
        self.v10Edit.setText("0")
        self.v11Edit.setText("0")
        self.xPosEdit.setText("0.00")
        self.yPosEdit.setText("0.00")
        QTimer.singleShot(0, lambda: self.redraw(posx=self.X, posy=self.Y))
        self.textBrowser.append(
            "> <span style='color: green'>Initialized successfully</span>\n"
        )


    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.redraw(posx=self.X, posy=self.Y)


    @Slot()
    def setSerialPort(self):
        if self.serialPort.isOpen():
            self.requestTimer.stop()
            self.serialPort.close()
            self.connectBtn.setText("Connect")
            self.textBrowser.append(
                "> <span style='color: green'>Serial port closed successfully</span>\n"
            )
            return
        self.serialPort.setPortName(self.portComboBox.currentText())
        if self.serialPort.open(QIODevice.OpenModeFlag.ReadWrite):
            self.connectBtn.setText("Disconnect")
            self.requestTimer.start(150)
            self.textBrowser.append(
                "> <span style='color: green'>Serial port connected successfully</span>\n"
            )
        else:
            self.textBrowser.append(
                "> <span style='color: red'>Serial port connection failed</span>\n"
            )
            QMessageBox.critical(self, "Error", "Failed to open serial port!")


    @Slot()
    def setResistance(self):
        text = self.resistanceBox.text().strip()
        value = int(text)
        nn = f"{value:02d}"
        cmd = f"#SI:{nn}%".encode('utf-8')  # check char #SI:nn%

        if self.serialPort.isOpen():
            self.serialPort.write(cmd)
            self.textBrowser.append(
                "> <span style='color:green'>Resistance set successfully</span>"
            )
        else:
            self.textBrowser.append(
                "> <span style='color: red'>Serial port not connected</span>\n"
            )
            QMessageBox.warning(self, "Warning", "Serial port not open!")


    @Slot()
    def readData(self):
        self.buffer += self.serialPort.readAll().data()
        
        while len(self.buffer) >= 12:
            data = self.buffer[:12]
            self.buffer = self.buffer[12:]

            v00 = self.parseVoltage(data[0], data[1], data[2])
            v01 = self.parseVoltage(data[3], data[4], data[5])
            v10 = self.parseVoltage(data[6], data[7], data[8])
            v11 = self.parseVoltage(data[9], data[10], data[11])

            self.v00Edit.setText(f"{v00}")
            self.v01Edit.setText(f"{v01}")
            self.v10Edit.setText(f"{v10}")
            self.v11Edit.setText(f"{v11}")

            self.calcPosition(v00, v01, v10, v11)  # change position

    
    @staticmethod
    def parseVoltage(c1: int, c2: int, c3: int) -> int:
        return (c1-48)*256 + (c2-48)*16 + (c3-48)


    @Slot()
    def requestData(self):
        if self.serialPort.isOpen():
            self.serialPort.write(b"#?data%")


    @Slot(QSerialPort.SerialPortError)
    def handleError(self, error):
        if error == QSerialPort.SerialPortError.ResourceError:
            self.textBrowser.append(
                "> <span style='color: red'>Serial port connection lost</span>\n"
            )
            QMessageBox.critical(self, "Error", "Serial port connection lost!")
            if self.serialPort.isOpen():
                self.requestTimer.stop()
                self.serialPort.close()
                self.connectBtn.setText("Connect")


    def calcPosition(self, v00: int, v01: int, v10: int, v11: int):
        sum_total = v00 + v01 + v10 + v11
        sum_left  = v00 + v10
        sum_right = v01 + v11
        sum_up    = v00 + v01
        sum_down  = v10 + v11

        x, y = 50.0, 50.0
        if sum_total != 0:
            x = ((sum_right-sum_left) / sum_total + 1.0) * 50.0
            y = ((sum_up-sum_down)    / sum_total + 1.0) * 50.0

        x = max(0.0, min(100.0, x))
        y = max(0.0, min(100.0, y))
        dx = self.calDisplacement(x)
        dy = self.calDisplacement(y)

        self.pxEdit.setText(f"{x:.2f}")
        self.pyEdit.setText(f"{y:.2f}")
        self.xPosEdit.setText(f"{dx:.2f}")
        self.yPosEdit.setText(f"{dy:.2f}")

        # set target position
        self.X = x
        self.Y = y
        self.redraw(posx=self.X, posy=self.Y)

    
    @staticmethod
    def calDisplacement(p: float):
        return 0.0176*p**3 - 2.6394*p**2 + 159.8415*p - 3591.1


    def redraw(self, posx=50.0, posy=50.0):
        self.clear()
        self.draw(posx, posy)


    def draw(self, posx=50.0, posy=50.0):
        rect = self.graphicsView.contentsRect()
        self.scene.setSceneRect(rect)

        view_rect = self.graphicsView.rect()
        center = view_rect.center()
        w = view_rect.width()
        h = view_rect.height()
        cx = center.x()
        cy = center.y()
        r = min(w, h) / 2 * 0.8

        # draw circle
        ring = self.scene.addEllipse(cx-r, cy-r, r*2, r*2, QPen(Qt.black, 2))

        # draw '+' line
        crossH = self.scene.addLine(cx-r, cy, cx+r, cy, QPen(Qt.black, 2))
        crossV = self.scene.addLine(cx, cy-r, cx, cy+r, QPen(Qt.black, 2))

        # draw target
        px = cx + (posx-50)*r/50
        py = cy - (posy-50)*r/50
        targetH = self.scene.addLine(px-15, py, px+15, py, QPen(Qt.red, 3))
        targetV = self.scene.addLine(px, py-15, px, py+15, QPen(Qt.red, 3))

        self.graphics_items.extend([
            ring,
            crossH, crossV,
            targetH, targetV,
        ])


    def clear(self):
        for item in self.graphics_items:
            self.scene.removeItem(item)
            del item
        self.graphics_items.clear()


    @Slot()
    def analysisData(self):
        total_rows = self.tableWidget.rowCount()
        if total_rows == 0:
            self.textBrowser.append(
                "> <span style='color: red'>There is no recorded " \
                "data in the table for analysis</span>\n"
            )
            QMessageBox.critical(
                self,
                "Analysis Error",
                "There is no recorded data in the table for analysis"
            )
            return

        x_data = []
        y_data = []
        for row in range(total_rows):
            x_item = self.tableWidget.item(row, 0)
            x_text = x_item.text().strip() if x_item else ""
            y_item = self.tableWidget.item(row, 1)
            y_text = y_item.text().strip() if y_item else ""

            try:
                x = float(x_text)
                y = float(y_text)
                x_data.append(x)
                y_data.append(y)
            except ValueError:
                continue

        if len(x_data) == 0 or len(y_data) == 0:
            self.textBrowser.append(
                "> <span style='color: red'>No valid numeric data available for plotting</span>\n"
            )
            QMessageBox.critical(
                self,
                "Analysis Error",
                "No valid numeric data available for plotting"
            )
            return
        
        span = float(self.moveEdit.text().strip())
        plot_dialog = PlotDialog(
            np.array(x_data), np.array(y_data),
            span=span, parent=self
        )
        plot_dialog.exec()


    @Slot()
    def recordData(self):
        dx = float(self.xPosEdit.text().strip())
        dy = float(self.yPosEdit.text().strip())

        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(f"{dx:.2f}"))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(f"{dy:.2f}"))


    @Slot()
    def deleteData(self):
        current_row = self.tableWidget.currentRow()
        if current_row == -1:
            return
        
        self.tableWidget.removeRow(current_row)


    @Slot()
    def clearData(self):
        self.tableWidget.setRowCount(0)


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
    def openData(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Excel File",
            "docs",  # default file path
            "Excel Files (*.xlsx);;All Files (*)"
        )
        if not file_path:
            return
        
        try:
            df = pd.read_excel(file_path)
            self.tableWidget.setRowCount(0)
            
            for row_idx, row_data in df.iterrows():
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)

                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(row_data.iloc[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(str(row_data.iloc[1])))
            self.textBrowser.append(
                "> <span style='color:green'>Data loaded successfully</span>"
            )

        except Exception as e:
            self.textBrowser.append(
                f"> <span style='color: red'>Failed to open file:\n{str(e)}</span>\n"
            )
            QMessageBox.critical(self, "Error", f"Failed to open file:\n{str(e)}")


    @Slot()
    def showHelp(self):
        help_text = """
    User Help Manual

    1. Data Entry
    Enter valid numbers in the two input boxes,
    then click the Record button to add data to the table with automatic numbering.

    2. Delete Row
    Select a row in the table, then click Delete
    to remove the selected row. The sequence number will auto reorder.

    3. Clear All
    Click Clear to empty all records in the table at once.

    4. Save to Excel
    Click Save to export all table data as an Excel file.

    5. Open Excel File
    Click Open to select a saved Excel file,
    the data will be loaded automatically into the table.

    6. Close Window
    Click Close to exit the current program window.

    Tip: Only numeric values are allowed; empty or invalid input will be ignored.
    """

        QMessageBox.information(self, "Help", help_text.strip())


    @Slot()
    def showAbout(self):
        about_text = """
    Laser Collimator
    Author: Jiahui Su
    Email: sjh855210@qq.com
    School: HFUT
    Version: 1.0

    A desktop application based on PySide6.
    Functions:
    - Input and record numeric data
    - Add, delete, clear table rows
    - Export table data to Excel
    - Import Excel data into table

    Developed with: Python + PySide6
    Copyright © 2026 All Rights Reserved.
    """

        QMessageBox.information(self, "About", about_text.strip())
