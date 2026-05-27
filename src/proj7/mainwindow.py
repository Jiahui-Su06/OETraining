from PySide6.QtGui import QPainter
from ui_mainwindow import Ui_MainWindow
from core import ViewGraphicsScene, LaserResonator
from PySide6.QtWidgets import QMainWindow, QMessageBox


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set default value
        self.wavelength_DSpinBox.setValue(1.046)
        self.cavity_length_DSpinBox.setValue(450.0)
        self.left_radius_DSpinBox.setValue(500.0)
        self.right_radius_DSpinBox.setValue(500.0)
        self.key_step_DSpinBox.setValue(20.0)
        self.d1Box.setValue(20.0)
        self.d2Box.setValue(100.0)
        self.fBox.setValue(40.0)
        
        self.scene = ViewGraphicsScene(self)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)

        wl = self.wavelength_DSpinBox.value()
        L = self.cavity_length_DSpinBox.value()
        r1 = self.left_radius_DSpinBox.value()
        r2 = self.right_radius_DSpinBox.value()
        d1 = self.d1Box.value()
        d2 = self.d2Box.value()
        f = self.fBox.value()
        lens = self.checkBox.isChecked()

        self.resonator = LaserResonator(
            parent_scene=self.scene,
            wl=wl, L=L, r1=r1, r2=r2,
            d1=d1, d2=d2, f=f, lens=lens
        )

        self.wavelength_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.cavity_length_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.left_radius_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.right_radius_DSpinBox.valueChanged.connect(self.redraw_scene)
        self.checkBox.toggled.connect(self.redraw_scene)
        self.d1Box.valueChanged.connect(self.redraw_scene)
        self.d2Box.valueChanged.connect(self.redraw_scene)
        self.fBox.valueChanged.connect(self.redraw_scene)
        self.help_Button.clicked.connect(self.show_help_dialog)
        self.reset_Button.clicked.connect(self.reset_Button_clicked)


    def zoom_in(self):
        self.graphicsView.scale(2, 2)


    def zoom_out(self):
        self.graphicsView.scale(0.5, 0.5)


    def redraw_scene(self):
        wl = self.wavelength_DSpinBox.value()
        L = self.cavity_length_DSpinBox.value()
        r1 = self.left_radius_DSpinBox.value()
        r2 = self.right_radius_DSpinBox.value()
        d1 = self.d1Box.value()
        d2 = self.d2Box.value()
        f = self.fBox.value()
        lens = self.checkBox.isChecked()

        self.resonator.update_params(
            wl=wl, L=L, r1=r1, r2=r2,
            d1=d1, d2=d2, f=f, lens=lens
        )
        z_waist_from_lens, waist_width = self.resonator.get_external_waist()
        self.wasitEdit.setText(f"{waist_width:.2f}")
        self.distanceEdit.setText(f"{z_waist_from_lens:.2f}")
        self.resonator.redraw()


    def show_help_dialog(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Function Key Introduction")
        msg_box.setText(
            "1. Use the left/right arrow keys to adjust cavity length.\n" \
            "2. Use the up/down arrow keys to adjust the radius of the right mirror.\n" \
            "3. Press the W/S keys to adjust the radius of the left mirror.\n" \
            "4. Hold Ctrl and scroll the mouse wheel to zoom the view.\n" \
            "5. Drag the left mirror to move the entire resonator.")
        msg_box.setIcon(QMessageBox.Information)

        msg_box.exec()


    def reset_Button_clicked(self):
        self.wavelength_DSpinBox.setValue(1.064)
        self.cavity_length_DSpinBox.setValue(450)
        self.left_radius_DSpinBox.setValue(500)
        self.right_radius_DSpinBox.setValue(500)
        self.key_step_DSpinBox.setValue(20)

        self.redraw_scene()
    