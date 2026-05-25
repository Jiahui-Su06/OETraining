from core import ViewGraphicsScene
from core.pixel_scaler import pixel_scaler
from PySide6.QtGui import QPen
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsRectItem


class Ruler:
    def __init__(
        self,
        parent_scene: ViewGraphicsScene,
        parent_item: QGraphicsRectItem,
        cursor: float = 225.0,
        x: float = 50.0,
        y: float = 300.0
    ):
        # scale length and select step, sub_step
        self.cursor = cursor
        self.steper()
        num_step = int(cursor//self.step) + 1
        num_sub_step = int(num_step*self.step/self.sub_step) + 1
        self.length = num_step * self.step
        length_scale, self.scale = pixel_scaler(self.length)
        cursor_scale = self.cursor * self.scale
        step_scale = self.step * self.scale
        sub_step_scale = self.sub_step * self.scale

        self.x = x
        self.y = y

        black_pen = QPen(Qt.black)
        black_pen.setWidth(2)

        scale_line = parent_scene.addLine(
            0 + self.x, 0 + self.y,
            length_scale + self.x, 0 + self.y,
            black_pen
        )
        scale_line.setParentItem(parent_item)

        l_step = 10
        l_sub_step = 5

        mark = [None,] * (num_step + 1)
        mark_num = [None,] * (num_step + 1)
        for i in range(num_step + 1):
            mark[i] = parent_scene.addLine(
                step_scale*i + self.x, self.y,
                step_scale*i + self.x, l_step + self.y,
                black_pen
            )
            mark[i].setParentItem(parent_item)
            mark_num[i] = parent_scene.addText(f"{i*self.step:.1f}")
            mark_num[i].setDefaultTextColor(Qt.black)
            mark_num[i].setPos(
                step_scale*i+self.x-10, l_step+self.y+5
            )
            mark_num[i].setParentItem(parent_item)

        
        mark_sub = [None,] * num_sub_step
        for i in range(num_sub_step):
            mark_sub[i] = parent_scene.addLine(
                sub_step_scale*i + self.x, self.y,
                sub_step_scale*i + self.x, l_sub_step + self.y,
                black_pen
            )
            mark_sub[i].setParentItem(parent_item)

        l_cursor = 20

        cursor_begin = parent_scene.addLine(
            self.x, self.y,
            self.x, self.y-l_cursor,
            black_pen
        )
        cursor_begin.setParentItem(parent_item)

        cursor_end = parent_scene.addLine(
            cursor_scale + self.x, self.y,
            cursor_scale + self.x, self.y-l_cursor,
            black_pen
        )
        cursor_end.setParentItem(parent_item)

        cursor_num = parent_scene.addText(f"{self.cursor}")
        cursor_num.setDefaultTextColor(Qt.black)
        cursor_num.setPos(self.x+5, self.y-25)
        cursor_num.setParentItem(parent_item)


    def steper(self):
        if self.cursor > 500:
            self.step = 100
            self.sub_step = 10
        elif 250 < self.cursor <= 500:
            self.step = 50
            self.sub_step = 5
        elif 50 < self.cursor <= 250:
            self.step = 50
            self.sub_step = 5
        else:
            self.step = 10
            self.sub_step = 1
        




