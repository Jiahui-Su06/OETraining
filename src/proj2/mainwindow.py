import os
import numpy as np
import pyvista as pv

from reconworker import ReconWorker
from ui_mainwindow import Ui_MainWindow
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import (
    QMainWindow, QGraphicsScene,
    QGraphicsView, QFileDialog,
    QMessageBox,
)

PIXEL_SIZE = 5.2e-3  # pixel size (mm)
LAMBDA = 650.0e-6  # wavelength (mm)
STEP = 0.2  # z direction sweep step (mm)


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

        self.openBtn.clicked.connect(self.openImage)
        self.processBtn.clicked.connect(self.processImage)

        self.actionOpen.triggered.connect(self.openImage)
        self.actionQuit.triggered.connect(self.close)
        self.actionHelp.triggered.connect(self.showHelp)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionProcess.triggered.connect(self.processImage)

        self.textBrowser.append(
            "> <span style='color: green'>Initialized successfully</span>\n"
        )


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


    @Slot()
    def processImage(self):
        if self.filePath is None:
            self.textBrowser.append(
                    "> <span style='color: red'>No image opened</span>\n"
                )
            QMessageBox.warning(self, "Error", "No image opened!")
            return
        
        try:
            z_start = float(self.zStartEdit.text().strip())
            z_end = float(self.zEndEdit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Error", "Z values must be numbers!")
            return
        
        self.processBtn.setEnabled(False)
        self.textBrowser.append(
            "> <span style='color:blue'>Start processing hologram... Please wait.</span>\n"
        )

        self.worker = ReconWorker(self.filePath, z_start, z_end)
        self.worker.progress_update.connect(self.proBar.setValue)
        self.worker.finished_data.connect(self.processFinished)
        self.worker.error_occurred.connect(self.processError)

        self.worker.start()


    @Slot(list)
    def processFinished(self, bubbles_3d):
        self.processBtn.setEnabled(True)
        self.proBar.setValue(0)
        self.textBrowser.append(
            "> <span style='color:green'>Processing finished successfully</span>\n"
        )

        N_SHOW = 20  # only show biggest 20 bubbles
        # key = 'r'  # 'r' for score
        key = 'score'

        if bubbles_3d:
            bubbles_3d_sorted = sorted(bubbles_3d, key=lambda b: b[key], reverse=True)
            bubbles_3d_show = bubbles_3d_sorted[:N_SHOW]

            xs = [b['x'] * PIXEL_SIZE  for b in bubbles_3d_show]
            ys = [b['y'] * PIXEL_SIZE  for b in bubbles_3d_show]
            zs = [b['z'] for b in bubbles_3d_show]
            rs = np.array([b['r'] * PIXEL_SIZE for b in bubbles_3d_show])

            points = np.column_stack((xs, ys, zs))
            poly = pv.PolyData(points)
            poly["Radius"] = rs

            bubble_geometry = poly.glyph(
                scale="Radius",
                factor=1.0,
                geom=pv.Sphere(radius=1.0, theta_resolution=20, phi_resolution=20),
                orient=False
            )

            plotter = pv.Plotter(title='3D Bubbles Show (largest 20)')
            plotter.add_mesh(
                bubble_geometry, 
                cmap='viridis',
                scalars="Radius",
                show_scalar_bar=True,
                scalar_bar_args={'title': 'Radius (mm)'},
                smooth_shading=True,
                specular=0.5
            )

            plotter.add_axes(xlabel='X (mm)', ylabel='Y (mm)', zlabel='Z (mm)')
            plotter.show_grid()
            plotter.set_background("white")
            plotter.show()
        else:
            self.textBrowser.append("> <span style='color:red'>There haven't bubbles</span>\n")


    @Slot(str)
    def processError(self, err_msg):
        self.processBtn.setEnabled(True)
        self.proBar.setValue(0)
        QMessageBox.critical(self, "Processing Error", f"An error occurred:\n{err_msg}")
        self.textBrowser.append(f"> <span style='color:red'>Error: {err_msg}</span>\n")


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