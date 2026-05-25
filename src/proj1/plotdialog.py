import numpy as np

from ui_plotdialog import Ui_Dialog
from PySide6.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas,
)
from matplotlib.figure import Figure


class PlotDialog(QDialog, Ui_Dialog):
    def __init__(self, dx, dy, span, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # X-direction
        layoutX = QVBoxLayout(self.xWidget)
        self.figureX = Figure()
        self.canvasX = FigureCanvas(self.figureX)
        layoutX.addWidget(self.canvasX)
        self.axesX = self.figureX.add_subplot(111)
        self.axesX_twin = self.axesX.twinx()
        z = np.arange(0, dx.size * span, span)

        # A = [z, 1]
        AX = np.vstack([z, np.ones(len(z))]).T
        kX, bX = np.linalg.lstsq(AX, dx, rcond=None)[0]
        dx_fit = kX * z + bX
        errorX = dx - dx_fit
        mseX = np.mean((errorX) ** 2)

        self.xEqEdit.setText(f"dx = {kX:.2f}*z {bX:+.2f}")
        self.xVarEdit.setText(f"{mseX:.2f}")

        lineX_orign = self.axesX.plot(
            z, dx,
            marker='o', linestyle='-',
            color='#1f77b4', linewidth=2,
            markersize=4, label='Original'
        )
        lineX_fit = self.axesX.plot(
            z, dx_fit,
            linestyle='--', color='#ff7f0e',
            linewidth=2, label='Linear Fit'
        )
        self.axesX.set_xlabel("Z (mm)")
        self.axesX.set_ylabel("dx (μm)")
        # self.axesX.set_title("X-direction")
        self.axesX.grid(True, alpha=0.3)

        lineX_error = self.axesX_twin.plot(
            z, errorX,
            marker='s', linestyle=':', 
            color='#2ca02c', linewidth=2.0, 
            markersize=4, label='Error'
        )
        self.axesX_twin.set_ylabel("Error (μm)", color='#2ca02c')
        self.axesX_twin.tick_params(axis='y', labelcolor='#2ca02c')

        linesX = lineX_orign + lineX_fit + lineX_error
        labelsX = [l.get_label() for l in linesX]
        self.axesX.legend(linesX, labelsX, loc='best')
        self.figureX.tight_layout()

        ############### Y-direction ###############
        layoutY = QVBoxLayout(self.yWidget)
        self.figureY = Figure()
        self.canvasY = FigureCanvas(self.figureY)
        layoutY.addWidget(self.canvasY)
        self.axesY = self.figureY.add_subplot(111)
        self.axesY_twin = self.axesY.twinx()
        z = np.arange(0, dy.size * span, span)

        # A = [z, 1]
        AY = np.vstack([z, np.ones(len(z))]).T
        kY, bY = np.linalg.lstsq(AY, dy, rcond=None)[0]
        dy_fit = kY * z + bY
        errorY = dy - dy_fit
        mseY = np.mean((errorY) ** 2)

        self.yEqEdit.setText(f"dy = {kY:.2f}*z {bY:+.2f}")
        self.yVarEdit.setText(f"{mseY:.2f}")

        lineY_orign = self.axesY.plot(
            z, dy,
            marker='o', linestyle='-',
            color='#1f77b4', linewidth=2,
            markersize=4, label='Original'
        )
        lineY_fit = self.axesY.plot(
            z, dy_fit,
            linestyle='--', color='#ff7f0e',
            linewidth=2, label='Linear Fit'
        )
        self.axesY.set_xlabel("Z (mm)")
        self.axesY.set_ylabel("dy (μm)")
        # self.axesY.set_title("Y-direction")
        self.axesY.grid(True, alpha=0.3)

        lineY_error = self.axesY_twin.plot(
            z, errorY,
            marker='s', linestyle=':', 
            color='#2ca02c', linewidth=2.0, 
            markersize=4, label='Error'
        )
        self.axesY_twin.set_ylabel("Error (μm)", color='#2ca02c')
        self.axesY_twin.tick_params(axis='y', labelcolor='#2ca02c')

        linesY = lineY_orign + lineY_fit + lineY_error
        labelsY = [l.get_label() for l in linesY]
        self.axesY.legend(linesY, labelsY, loc='best')
        self.figureY.tight_layout()


    