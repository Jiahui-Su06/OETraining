from core import ViewGraphicsScene, LaserBeam, Ruler
from PySide6.QtGui import QPen, QBrush, QPainterPath
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsItem


class LaserResonator(LaserBeam):
    def __init__(
        self,
        parent_scene: ViewGraphicsScene,
        wl: float = 1.064, # um Nd:YAG laser
        L:  float = 450.0, # mm
        r1: float = 500.0, # mm (np.inf or 0 is plate mirror)
        r2: float = 500.0, # mm (np.inf or 0 is plate mirror)
        x: float = 50.0,   # origin point's (x,y)
        y: float = 300.0,
        d1: float = 20.0,  # mm, gap length 
        f: float = 40.0,   # mm, focal length of lens
        d2: float = 100.0, # mm, view length
        lens: bool = False # yes or not lens
    ):
        super().__init__(
            wl=wl,
            L=L,
            r1=r1,
            r2=r2,
            d1=d1,
            f=f,
            d2=d2,
            lens=lens
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
        
        mirror_left = self.scene.addRect(
            self.x-self.thick_mirror, self.y-self.w_mirror,
            self.thick_mirror, self.w_mirror*2,
            blue_pen
        )
        ruler = Ruler(
            parent_scene=self.scene,
            parent_item=mirror_left,
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

        mirror_right.setParentItem(mirror_left)
        normal.setParentItem(mirror_left)
        mirror_left.setZValue(1)
        mirror_right.setZValue(1)
        normal.setZValue(0)
        mirror_left.setFlag(QGraphicsItem.ItemIsMovable)

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
        beam_up_item.setParentItem(mirror_left)
        beam_down_item.setParentItem(mirror_left)

        radius_left = self.scene.addText(f"{self.r1:.0f}")
        radius_left.setDefaultTextColor(Qt.black)
        radius_left.setPos(self.x, self.y+self.w_mirror)
        radius_left.setParentItem(mirror_left)

        radius_right = self.scene.addText(f"{self.r2:.0f}")
        radius_right.setDefaultTextColor(Qt.black)
        radius_right.setPos(self.x+L_scale+self.thick_mirror, self.y+self.w_mirror)
        radius_right.setParentItem(mirror_left)

        self.mirror_left = mirror_left
        self.mirror_right = mirror_right
        
        self.graphics_items.extend([
            mirror_left
        ])

        z_bef, w_bef, z_aft, w_aft = self.external_beam(self.d1, self.f, self.d2)
        
        if z_bef is not None and self.lens:
            x_m2 = self.x + L_scale 
            
            # draw beam between output mirror and lens
            beam_out_up = QPainterPath()
            beam_out_down = QPainterPath()
            beam_out_up.moveTo(x_m2, self.y + w_bef[0]*self.scale)
            beam_out_down.moveTo(x_m2, self.y - w_bef[0]*self.scale)
            
            for i in range(1, len(z_bef)):
                curr_x = x_m2 + z_bef[i]*ruler.scale
                beam_out_up.lineTo(curr_x, self.y + w_bef[i]*self.scale)
                beam_out_down.lineTo(curr_x, self.y - w_bef[i]*self.scale)
            
            out_up_item = self.scene.addPath(beam_out_up, QPen(Qt.green, 2))
            out_down_item = self.scene.addPath(beam_out_down, QPen(Qt.green, 2))
            out_up_item.setParentItem(mirror_left)
            out_down_item.setParentItem(mirror_left)

            # position of lens
            x_lens = x_m2 + self.d1 * ruler.scale
            
            # draw lens
            lens_height = self.w_mirror * 2
            lens_width = 8
            lens_item = self.scene.addEllipse(
                x_lens-lens_width/2, self.y-lens_height/2, 
                lens_width, lens_height, QPen(Qt.blue, 2)
            )
            lens_item.setParentItem(mirror_left)
            lens_item.setZValue(2)
            
            # draw beam behind lens
            beam_aft_up = QPainterPath()
            beam_aft_down = QPainterPath()
            beam_aft_up.moveTo(x_lens, self.y+w_aft[0]*self.scale)
            beam_aft_down.moveTo(x_lens, self.y-w_aft[0]*self.scale)
            
            for i in range(1, len(z_aft)):
                curr_x = x_lens + z_aft[i]*ruler.scale
                beam_aft_up.lineTo(curr_x, self.y+w_aft[i]*self.scale)
                beam_aft_down.lineTo(curr_x, self.y-w_aft[i]*self.scale)
                
            aft_up_item = self.scene.addPath(beam_aft_up, QPen(Qt.green, 2))
            aft_down_item = self.scene.addPath(beam_aft_down, QPen(Qt.green, 2))
            aft_up_item.setParentItem(mirror_left)
            aft_down_item.setParentItem(mirror_left)
            
            f_text = self.scene.addText(f"f={self.f}mm")
            f_text.setDefaultTextColor(Qt.blue)
            f_text.setPos(x_lens, self.y-lens_height/2-25)
            f_text.setParentItem(mirror_left)
