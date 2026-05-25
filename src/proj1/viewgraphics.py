from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPainter, QPen


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPosition(x=50, y=50)

    def drawTargetRing(self, posx=50.0, posy=50.0):
        center = self.viewport().rect().center()
        cx = center.x()
        cy = center.y()

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w = self.viewport().rect().width()
        h = self.viewport().rect().height()
        r = min(w, h) / 2 - 30

        # draw circle
        painter.setPen(QPen(Qt.black, 2))
        painter.drawEllipse(cx-r, cy-r, r*2, r*2)

        # draw '+' line
        painter.drawLine(cx-r, cy, cx+r, cy)
        painter.drawLine(cx, cy-r, cx, cy+r)

        # draw text
        painter.drawText(cx-r/2, cy-r/2, "D00")
        painter.drawText(cx+r/2, cy-r/2, "D01")
        painter.drawText(cx-r/2, cy+r/2, "D10")
        painter.drawText(cx+r/2, cy+r/2, "D11")

        # draw target
        px = cx + (posx-50)*r/50
        py = cy - (posy-50)*r/50
        painter.setPen(QPen(Qt.red, 3))
        painter.drawLine(px-15, py, px+15, py)
        painter.drawLine(px, py-15, px, py+15)

    def setPosition(self, x:int=50, y:int=50):
        self.X = x
        self.Y = y
        self.drawTargetRing(posx=self.X, posy=self.Y)









