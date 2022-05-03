#It is possible to either change feature’s geometry or to change some attributes.
#The following example first changes values of attributes with index 0 and 1,
#then it changes the feature’s geometry.
# koristeni lejer = Osnovne skole na 5km copy
layer = iface.activeLayer()
caps = layer.dataProvider().capabilities()

fid = 17   # ID of the feature we will modify

if caps & QgsVectorDataProvider.ChangeAttributeValues:
    attrs = { 0 : 3 , 1 : "Moja skola" }
    layer.dataProvider().changeAttributeValues({ fid : attrs })

if caps & QgsVectorDataProvider.ChangeGeometries:
    geom = QgsGeometry.fromPointXY(QgsPointXY(7436734,5006204))
    layer.dataProvider().changeGeometryValues({ fid : geom })

# ukoliko se rezultat ne pojavi na gui potrebno je osveziti
if iface.mapCanvas().isCachingEnabled():
    layer.triggerRepaint()
else:
    iface.mapCanvas().refresh()   


