import os
import cv2
import numpy as np

from PIL import Image, ImageFont, ImageDraw
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap, QPainter, QImage
from ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import (
    QMainWindow, QFileDialog, QGraphicsScene,
    QGraphicsView, QMessageBox
)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)

        self.filePath = None
        self.imageItem = None

        self.openBtn.clicked.connect(self.openImage)
        self.processBtn.clicked.connect(self.processImage)
        self.saveBtn.clicked.connect(self.saveImage)

        self.actionOpen.triggered.connect(self.openImage)
        self.actionSave.triggered.connect(self.saveImage)
        self.actionClose.triggered.connect(self.close)
        self.actionProcess.triggered.connect(self.processImage)
        self.actionHelp.triggered.connect(self.showHelp)
        self.actionAbout.triggered.connect(self.showAbout)


    @Slot()
    def openImage(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "images",
            "Image File (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if not self.filePath:
            return
        
        self.textBrowser.append(
            f"> <span style='color:green'>Image file {os.path.basename(self.filePath)} opened successfully\n</span>"
        )
        pixmap = QPixmap(self.filePath)
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.graphicsView.resetTransform()  # set to 1.0 scale
        self.graphicsView.scale(0.5, 0.5)


    @Slot()
    def processImage(self):
        if self.filePath is None:
            self.textBrowser.append(
                    "> <span style='color: red'>No image opened</span>\n"
                )
            QMessageBox.warning(self, "Error", "No image opened!")
            return
        img = cv2.imread(self.filePath)
        
        h, w = img.shape[:2]
        cx = w // 2
        cy = h // 2
        cover = min(w, h) // 4
        img[cy-cover:cy+cover, cx-cover:cx+cover] = 0

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        gap_points = []
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            if len(approx) < 8:
                for point in approx:
                    x, y = point[0]
                    gap_points.append((x, y))
        
        corners = [
            (0, 0), (w-1, 0),
            (0, h-1), (w-1, h-1)
        ]

        for corner in corners:
            gap_points = self.removePoints(gap_points, corner, n=2)

        # # Mark all gap points
        # for pt in gap_points:
        #     cv2.circle(img, pt, 4, (0, 0, 255), -1)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        draw = ImageDraw.Draw(img)

        font_path = "C:/Windows/Fonts/times.ttf"
        font = ImageFont.truetype(font_path, 30)

        used = set()
        for i, pt1 in enumerate(gap_points):
            min_dist = float('inf')
            min_j = -1
            for j, pt2 in enumerate(gap_points):
                if i == j:
                    continue
                dist = np.linalg.norm(np.array(pt1) - np.array(pt2))
                if dist < min_dist:
                    min_dist = dist
                    min_j = j
            key = tuple(sorted([i, min_j]))
            if min_j != -1 and key not in used:
                used.add(key)
                pt2 = gap_points[min_j]
                mid_x = (pt1[0] + pt2[0]) // 2
                mid_y = (pt1[1] + pt2[1]) // 2
                gap_size = int(np.linalg.norm(np.array(pt1) - np.array(pt2)))
                draw.text((mid_x+10, mid_y-20), str(gap_size), font=font, fill=(255, 255, 255))
        
        self.displayImage(np.array(img))


    def displayImage(self, rgb_array):
        h, w, ch = rgb_array.shape
        bytes_per_line = ch * w

        q_img = QImage(rgb_array.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)

        self.scene.clear()
        self.imageItem = self.scene.addPixmap(pixmap)


    @Slot()
    def saveImage(self):
        if self.imageItem is None:
            QMessageBox.warning(self, "Error", "No processed images found, please process images first!")
            return
        
        file_name = os.path.splitext(os.path.basename(self.filePath))[0]
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save processed image", f"./results/{file_name}_processed.bmp", "Images (*.bmp *.png *.jpg)"
        )

        if file_path:
            pixmap = self.imageItem.pixmap()
            if pixmap.save(file_path):
                self.textBrowser.append(f"> <span style='color: green'>Image saved successfully to: {file_path}</span>\n")
            else:
                QMessageBox.critical(self, "Error", "Failed to save image!")


    @staticmethod
    def removePoints(points, corner, n=2):
        dists = [np.hypot(pt[0] - corner[0], pt[1] - corner[1]) for pt in points]
        idx_sorted = np.argsort(dists)
        remove_idx = idx_sorted[:n]

        for idx in sorted(remove_idx, reverse=True):
            points.pop(idx)
        return points


    def wheelEvent(self, event):
        if not event.modifiers() & Qt.ControlModifier:
            event.ignore()
            return
        
        zoom_factor = 1.2
        if event.angleDelta().y() > 0:
            self.graphicsView.scale(zoom_factor, zoom_factor)
        else:
            self.graphicsView.scale(1/zoom_factor, 1/zoom_factor)


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
