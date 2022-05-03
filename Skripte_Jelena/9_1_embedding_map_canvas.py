#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# canvas.html#embedding-map-canvas

''' The Map canvas widget is probably the most important widget within QGIS because it shows the
map composed from overlaid map layers and allows interaction with the map and layers.
The canvas always shows a part of the map defined by the current canvas extent.
The interaction is done through the use of map tools: there are tools for panning, zooming,
identifying layers, measuring, vector editing and others. Similar to other graphics programs,
there is always one tool active and the user can switch between the available tools.
The map canvas is implemented with the QgsMapCanvas class in the qgis.gui module.
The implementation is based on the Qt Graphics View framework.
This framework generally provides a surface and a view where custom graphics items are placed and user can
interact with them. We will assume that you are familiar enough with Qt to understand the concepts of the graphics
scene, view and items.
If not, please read the overview of the framework''' 

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
canvas.setLayers([layer])
# ucitao je celokupan prikaz lejera okrug_copy na samostalno otvorenom
# radnom okruzenju  mape

