# -*- coding: cp1252 -*-
#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# canvas.html#using-map-tools-with-canvas

''' The following example constructs a window that contains a map canvas and
basic map tools for map panning and zooming. Actions are created for activation
of each tool: panning is done with QgsMapToolPan, zooming in/out with a pair of
QgsMapToolZoom instances. The actions are set as checkable and later assigned to
the tools to allow automatic handling of checked/unchecked state of the actions
– when a map tool gets activated, its action is marked as selected and the
action of the previous map tool is deselected.
The map tools are activated using setMapTool() method'''

'''from qgis.gui import *
from qgis.PyQt.QtWidgets import QAction, QMainWindow
from qgis.PyQt.QtCore import Qt'''

''' #prethodni koraci 
canvas = QgsMapCanvas()
canvas.show()
# otvara samostalno radno okruzenje 

canvas.setCanvasColor(Qt.white)
canvas.enableAntiAliasing(True)

# korisceni lejer = Okrug_copy
layer = iface.activeLayer()

if not layer.isValid():
    print('Lejer nije uspesno ucitan')
# nema odgovora na komandu, nastavljam dalje da ucitavam komande

# namesta obim po ucitanom lejeru
canvas.setExtent(layer.extent())
# nista se ne desava ni u samostalnom niti u klasiicnoj radnoj mapi

# podesava lejere za "platno" mape
canvas.setLayers([layer]) '''
# ucitavanje prethodnog koraka i kasnije definisanje pomocu
# ispitivanih komandi takodje ne daje rezultat


layer = QgsProject.instance().mapLayersByName('Okrug_copy')[0]

class MojProzor(QMainWindow):
    def __init__(self, layer):
        QMainWindow.__init__(self)

        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(Qt.white)

        self.canvas.setExtent(layer.extent())
        self.canvas.setLayers([layer])

        self.setCentralWidget(self.canvas)

        self.actionZoomIn = QAction("Detaljnije", self)
        self.actionZoomOut = QAction("Manje_detaljno", self)
        self.actionPan = QAction("Pomeri", self)

        self.actionZoomIn.setCheckable(True)
        self.actionZoomOut.setCheckable(True)
        self.actionPan.setCheckable(True)

        self.actionZoomIn.triggered.connect(self.zoomIn)
        self.actionZoomOut.triggered.connect(self.zoomOut)
        self.actionPan.triggered.connect(self.pan)

        self.toolbar = self.addToolBar("Canvas actions")
        self.toolbar.addAction(self.actionZoomIn)
        self.toolbar.addAction(self.actionZoomOut)
        self.toolbar.addAction(self.actionPan)

# create the map tools
# kreira alate za mapu
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(self.actionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(self.actionZoomOut)

        self.pan()

    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)
    
# skripta ne radi, izbacuje greske od pocetka

w = MojProzor(layer)
w.show()
# ova komanda otvara prozor








