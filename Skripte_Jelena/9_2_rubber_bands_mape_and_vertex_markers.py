#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# canvas.html#rubber-bands-and-vertex-markers

''' To show some additional data on top of the map in canvas, use map canvas
items. It is possible to create custom canvas item classes (covered below),
however there are two useful canvas item classes for convenience:
QgsRubberBand for drawing polylines or polygons, and
QgsVertexMarker for drawing points.
They both work with map coordinates, so the shape is moved/scaled
automatically when the canvas is being panned or zoomed'''

#prethodni koraci 
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


# To show a polyline
# prikaz polilinije
linije = QgsRubberBand(canvas, False) # False oznacava da nije poligon
tacke = [
QgsPoint(7473760, 4978473), 
QgsPoint(7598538, 4871429), 
QgsPoint(7481447, 4971895)
]
linije.setToGeometry(QgsGeometry.fromPolyline(tacke), None)
linije.setWidth(3)
linije.setColor(QColor(255,255,255))

poligon = QgsRubberBand(canvas, True) # True oznacava da je u pitanju poligon
tacke = [
[QgsPointXY(7467763,4972398), 
QgsPointXY(7483588,4974579), 
QgsPointXY(7470046,4970009)]
]
poligon.setToGeometry(QgsGeometry.fromPolygonXY(tacke), None)
poligon.setColor(QColor(255,0,0))

# ukoliko zelimo da "sakrijemo" odredjeni item
poligon.hide()

# ukoliko zelimo da prikazemo odredjeni item
poligon.show()

# ukoliko zelimo da uklonimo lejer iz scene
#canvas.scene().removeItem(tacke)
#ne ucitava poslednju komandu











