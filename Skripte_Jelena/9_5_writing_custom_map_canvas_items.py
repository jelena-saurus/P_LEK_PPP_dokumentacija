# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# canvas.html#writing-custom-map-canvas-items

# Here is an example of a custom canvas item that draws a circle
# kreira item koji crta krug

class CircleCanvasItem(QgsMapCanvasItem):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.center = QgsPoint(0, 0)
        self.size = 100
    
    def setCenter(self, center):
        self.center = center
    
    def center(self):
        return sefl.center
    
    def setSize(self, size):
        self.size = size
    
    def size(self):
        return self.size
    
    def boundingRect(self):
        return QRectF(
        self.center.x() - self.size/2,
        self.center.y() - self.size/2,
        self.center.x() + self.size/2,
        self.center.y() + self.size/2
        )
        
    def paint(self, painter, option, widget):
        path = QPainterPath()
        path.moveTo(self.center.x(), self.center.y())
        path.arcTo(self.boundingRect(), 0.0, 360.0)
        painter.fillPath(path, QColor('red'))


item = CircleCanvasItem(iface.mapCanvas())
item.setCenter(QgsPointXY(7362758,4935009))
item.setSize(100)

# skripta ne radi, vraca gresku od pocetka


