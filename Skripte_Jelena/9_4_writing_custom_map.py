# https://docs.qgis.org/3.22/en/docs/
# pyqgis_developer_cookbook/canvas.html#writing-custom-map-tools
 """ You can write your custom tools, to implement a custom behavior
to actions performed by users on the canvas.  """


# definise alat koji kreira pravougaonik, proizvolje velicine
# i stampa njegove koordinate u konzolu

class RectangleMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberBand = QgsRubberBand(self.canvas, True)
        self.rubberBand.setColor(Qt.red)
        self.rubberBand.setWidth(1)
        self.reset()
    
    def reset(self):
        self.startPoint = self.endPoint = None
        self.isEmittingPoint = None
        self.rubberBand.reset(True)
    
    def canvasPressEvent(self, e):
        self.startPoint = self.toMapCoordinates(e.pos())
        self.endPoint = self.startPoint
        self.isEmittingPoint = True
        self.showRect(self.startPoint, self.endPoint)
    
    def canvasReleaseEvent(self, e):
        self.isEmittingPoint = False
        r = self.rectangle()
        if r is not None:
            print('Pravougaonik: ', r.xMinimum(), r.yMinimum(), r.xMaximum(), r.yMaximum())
    
    def canvasMoveEvent(self, e):
        if not self.isEmittingPoint:
            return
        
        self.endPoint = self.toMapCoordinates(e.pos())
        self.showRect(self.startPoint, self.endPoint)
    
    def showRect(self, startPoint, endPoint):
        self.rubberBand.reset(QgsWkbTypes.PolygonGeometry)
        if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
            return
        
        tacka1 = QgsPointXY(startPoint.x(), startPoint.y())
        tacka2 = QgsPointXY(startPoint.x(), endPoint.y())
        tacka3 = QgsPointXY(endPoint.x(), endPoint.y())
        tacka4 = QgsPointXY(endPoint.x(), startPoint.y())
        
        self.rubberBand.addPoint(tacka1, False)
        self.rubberBand.addPoint(tacka2, False)
        self.rubberBand.addPoint(tacka3, False)
        self.rubberBand.addPoint(tacka4, True) # True azurira platno
        self.rubberBand.show()
    
    def rectangle(self):
        if self.startPoint is None or self.endPoint is None:
            return None
        elif (
        self.startPoint.x() == self.endPoint.y() or \
        self.startPoint.y() == self.endPoint.y()
        ):
            return None
            
            return QgsRectangle(self.startPoint, self.endPoint)
    
    def deactivate(self):
        QgsMapTool.deactivate(self)
        self.deactivated.emit()

canvas = iface.mapCanvas()
x = RectangleMapTool(canvas)
canvas.setMapTool(x)
# skripta ne radi, vraca greske       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
