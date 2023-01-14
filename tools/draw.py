import sys ,random

from PyQt6 import QtCore,QtGui,QtWidgets
from  PyQt6.QtCore import Qt 


settings = {
    "size": 64,
    "resolution":10,
    "colors":["#000000",
              "#141923",
                "#414168",
                "#3a7fa7",
                "#35e3e3",
                "#8fd970",
                "#5ebb49",
                "#458352",
                "#dcd37b",
                "#fffee5",
                "#ffd035",
                "#cc9245",
                "#a15c3e",
                "#a42f3b",
                "#f45b7a",
                "#c24998",
                "#81588d",
                "#bcb0c2",
                "#ffffff",],
}

SPRAY_PARTICLES=100
SPRAY_DIAMETER = 10

class Canvas(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self._pixmap = QtGui.QPixmap(600,300)
        self._pixmap.fill(Qt.GlobalColor.white)
        self.setPixmap(self._pixmap)

        self.pen_color = QtGui.QColor("#000000")

    def set_pen_color(self,c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self,e):
        pos = e.position()
        painter = QtGui.QPainter(self._pixmap)
        p = painter.pen()
        p.setWidth(1)
        p.setColor(self.pen_color)
        painter.setPen(p)

        for n in range(SPRAY_PARTICLES):
            xo = random.gauss(0,SPRAY_DIAMETER)
            yo = random.gauss(0,SPRAY_DIAMETER)

            painter.drawPoint(pos.x()+xo,pos.y()+yo)

        self.setPixmap(self._pixmap)

class Drawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.c=Canvas()
        self.setCentralWidget(self.c)

    

    
    
app = QtWidgets.QApplication(sys.argv)
window= Drawer()
window.show()
app.exec()