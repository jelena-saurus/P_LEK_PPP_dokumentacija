# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# geometry.html#access-to-geometry

# kreiranje geometrije iz koordinata
gTacka = QgsGeometry.fromPointXY(QgsPointXY(7473975,4978647))
print(gTacka)
gLinija = QgsGeometry.fromPolyline([QgsPoint(7475894,4978697), QgsPoint(7479230,4978285)])
print(gLinija)
gPoligon = QgsGeometry.fromPolygonXY([
[QgsPointXY(7459602,4977949), 
QgsPointXY(7456506,4979147),
QgsPointXY(7464291,5004586)]])
print(gPoligon)

# First, you should find out the geometry type. The wkbType() method
# is the one to use. It returns a value from the QgsWkbTypes.Type enumeration.
# proverava tip geometrije
if gTacka.wkbType() == QgsWkbTypes.Point:
    print(gTacka.wkbType())
# output: 1 for Point
# izlaz: 1 za tacku

if gLinija.wkbType() == QgsWkbTypes.LineString:
    print(gLinija.wkbType())
# output: 2 for LineString
# izlaz: 2 za liniju

if gPoligon.wkbType() == QgsWkbTypes.Polygon:
    print(gPoligon.wkbType())
# output: 3 for Polygon
# izlaz: 3 za poligon



# As an alternative, one can use the type() method which returns a
# value from the QgsWkbTypes.GeometryType enumeration
# alternativni nacin

print(QgsWkbTypes.displayString(gTacka.wkbType()))
# izlaz: Point

print(QgsWkbTypes.displayString(gLinija.wkbType()))
# izlaz: LineString

print(QgsWkbTypes.displayString(gPoligon.wkbType()))
# izlaz:Polygon

# metode za pristup svakom vektorskom tipu torke predstavljanje
# u vidu XY koordinata nisu prave torke vec QgsPoint objekti, cijim
# vrednostima se moze pristupiti pomocu x() i y() metodama
print(gTacka.asPoint())
print(gLinija.asPolyline())
print(gPoligon.asPolygon())

# For multipart geometries there are similar accessor functions: asMultiPoint(),
# asMultiPolyline() and asMultiPolygon().
# za multipart geometrije to su: asMultiPoint(), asMultiPolyline(),
# asMultiPolygon()

# vrsi iteraciju nad svim delovima geometrije
for deo in gPoligon.parts():
    print(deo.asWkt())
