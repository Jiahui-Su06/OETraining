from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtCore import Qt


class ViewGraphicsScene(QGraphicsScene):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window


    def wheelEvent(self, event):
        if not event.modifiers() & Qt.ControlModifier:
            event.ignore()
            return
        
        num_pixels = event.delta()

        if num_pixels > 0 :
            self.main_window.zoom_in()
        if num_pixels < 0 :
            self.main_window.zoom_out()

        event.accept()
    
    
    def keyPressEvent(self, event):
        if not self.main_window.resonator.mirror_right:
            super().keyPressEvent(event)
            return

        wl = self.main_window.wavelength_DSpinBox.value()
        L  = self.main_window.cavity_length_DSpinBox.value()
        r1 = self.main_window.left_radius_DSpinBox.value()
        r2 = self.main_window.right_radius_DSpinBox.value()
        step = self.main_window.key_step_DSpinBox.value()

        if event.key() == Qt.Key_Left:
            L -= step
        elif event.key() == Qt.Key_Right:
            L += step
        elif event.key() == Qt.Key_W:
            r1 += step
        elif event.key() == Qt.Key_S:
            r1 -= step
        elif event.key() == Qt.Key_Up:
            r2 += step
        elif event.key() == Qt.Key_Down:
            r2 -= step
        else:
            super().keyPressEvent(event)
            return
        
        self.main_window.cavity_length_DSpinBox.setValue(L)
        self.main_window.left_radius_DSpinBox.setValue(r1)
        self.main_window.right_radius_DSpinBox.setValue(r2)

        self.main_window.resonator.update_params(wl=wl, L=L, r1=r1, r2=r2)
        self.main_window.resonator.redraw()
    
