# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/geometry.html#
# Geometry Handling

# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# geometry.html#geometry-construction

# PyQGIS provides several options for creating a geometry from coordinates
# kreiranje geometrije iz koordinata
gTacka = QgsGeometry.fromPointXY(QgsPointXY(7473975,4978647))
print(gTacka)
# QgsGeometry: Point (7473975 4978647)>

gLinija = QgsGeometry.fromPolyline([QgsPoint(7475894,4978697), QgsPoint(7479230,4978285)])
print(gLinija)
# QgsGeometry: LineString (7475894 4978697, 7479230 4978285)

gPoligon = QgsGeometry.fromPolygonXY([
[QgsPointXY(7459602,4977949), 
QgsPointXY(7456506,4979147),
QgsPointXY(7464291,5004586)]
])
print(gPoligon)
# QgsGeometry: Polygon ((7459602 4977949, 7456506 4979147, 7464291 5004586, 7459602 4977949)

# WKT - well-known text format (vise na https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)
geom_iz_wkt = QgsGeometry.fromWkt('POINT(7464925.5 4972209.4)')
print(geom_iz_wkt)
# QgsGeometry: Point (7464925.5 4972209.40000000037252903

# WKB - well-known binary format (https://mariadb.com/kb/en/well-known-binary-wkb-format/)
geom = QgsGeometry()
wkb = bytes.fromhex("010100000000000000000045400000000000001440")
geom.fromWkb(wkb)
print(geom.asWkt())
# Point (42 5)

