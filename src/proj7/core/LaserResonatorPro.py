from core import ViewGraphicsScene, LaserBeam, Ruler
from PySide6.QtGui import QPen, QBrush, QPainterPath
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsItem


class LaserResonatorPro(LaserBeam):
    def __init__(
        self,
        parent_scene: ViewGraphicsScene,
        wl: float = 1.064, # um Nd:YAG laser
        L:  float = 450.0, # mm
        r1: float = 500.0, # mm (np.inf or 0 is plate mirror)
        r2: float = 500.0, # mm (np.inf or 0 is plate mirror)
        x: float = 50.0,   # origin point's (x,y)
        y: float = 300.0,
    ):
        super().__init__(
            wl=wl,
            L=L,
            r1=r1,
            r2=r2
        )
        self.x, self.y = x, y
        self.scene = parent_scene
        self.scale = 150

        self.graphics_items = []

        self.redraw()


    def redraw(self):
        self.clear()
        self.draw()


    def clear(self):

        for item in self.graphics_items:
            self.scene.removeItem(item)
            del item
        self.graphics_items.clear()


    def draw(self):
        # make pen and brush
        blue_pen = QPen(Qt.blue, 2)
        red_pen  = QPen(Qt.red, 2)
        # red_brush = QBrush(Qt.red)

        z, w = self.beam_radius()
        w_max = max(w[0], w[-1]) if len(w) > 0 else 0
        self.w_mirror = w_max * 1.5 * self.scale if w_max > 0 else 20
        self.thick_mirror = 5
        
        mirror_1 = self.scene.addRect(
            self.x-self.thick_mirror, self.y-self.w_mirror,
            self.thick_mirror, self.w_mirror*2,
            blue_pen
        )
        ruler = Ruler(
            parent_scene=self.scene,
            parent_item=mirror_1,
            cursor=self.L,
            x=self.x,
            y=self.y+self.w_mirror+50
        )
        L_scale = self.L * ruler.scale
        mirror_right = self.scene.addRect(
            self.x+L_scale, self.y-self.w_mirror,
            self.thick_mirror, self.w_mirror*2,
            blue_pen,
            # red_brush
        )
        normal = self.scene.addLine(
            self.x, self.y,
            self.x+L_scale, self.y,
            red_pen
        )

        mirror_right.setParentItem(mirror_1)
        normal.setParentItem(mirror_1)
        mirror_1.setZValue(1)
        mirror_right.setZValue(1)
        normal.setZValue(0)
        mirror_1.setFlag(QGraphicsItem.ItemIsMovable)

        beam_up = QPainterPath()
        beam_down = QPainterPath()
        beam_up.moveTo(self.x+z[0]*ruler.scale, self.y+w[0]*self.scale)
        beam_down.moveTo(self.x+z[0]*ruler.scale, self.y-w[0]*self.scale)

        for i in range(1, len(z)):
            beam_up.lineTo(self.x+z[i]*ruler.scale, self.y+w[i]*self.scale)
            beam_down.lineTo(self.x+z[i]*ruler.scale, self.y-w[i]*self.scale)

        beam_up_item = self.scene.addPath(beam_up)
        beam_up_item.setPen(blue_pen)
        beam_down_item = self.scene.addPath(beam_down)
        beam_down_item.setPen(blue_pen)
        beam_up_item.setParentItem(mirror_1)
        beam_down_item.setParentItem(mirror_1)

        radius_left = self.scene.addText(f"{self.r1:.0f}")
        radius_left.setDefaultTextColor(Qt.black)
        radius_left.setPos(self.x, self.y+self.w_mirror)
        radius_left.setParentItem(mirror_1)

        radius_right = self.scene.addText(f"{self.r2:.0f}")
        radius_right.setDefaultTextColor(Qt.black)
        radius_right.setPos(self.x+L_scale+self.thick_mirror, self.y+self.w_mirror)
        radius_right.setParentItem(mirror_1)

        self.mirror_left = mirror_1
        self.mirror_right = mirror_right
        
        self.graphics_items.extend([
            mirror_1
        ])

