# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#modifying-vector-layers
# koristen lejer - Osnovne skole na 5km copy
layer = iface.activeLayer()


# proverava da li je odredjena funkcija podrzana
caps = layer.dataProvider().capabilities()

if caps and QgsVectorDataProvider.AddAttributes:
    print('Lejer podrzava dodavanje atributa!')

# Proverava sve moguce funkcije lejera    
caps_string = layer.dataProvider().capabilitiesString()
print(caps_string)
# stampa sve funkcije sa lejerima
# Add Features, Delete Features, Change Attribute Values, Add Attributes, Delete Attributes,
# Rename Attributes, Create Spatial Index,Create Attribute Indexes, 
# Fast Access to Features at ID, Change Geometries

# VAZNA NAPOMENA
# If you are working inside QGIS It might be necessary to force a redraw of the map canvas
# in order to see the changes you’ve done to the geometry, to the style or to the attributes:
# If caching is enabled, a simple canvas refresh might not be sufficient
# to trigger a redraw and you must clear the cached image for the layer
if iface.mapCanvas().isCachingEnabled():
    layer.triggerRepaint()
else:
    iface.mapCanvas().refresh()


# 6.4.1. Add Features
# dodavanje featurea
if caps and QgsVectorDataProvider.AddFeatures:
    feat = QgsFeature(layer.fields())
    feat.setAttribute(0, 3)
    feat.setAttribute(1, 'Moja skola')
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(7476420,5010415)))
    (res, outFeats) = layer.dataProvider().addFeatures([feat])

#i featurea koji cu kasnije izbrisati
if caps and QgsVectorDataProvider.AddFeatures:
    feat = QgsFeature(layer.fields())
    feat.setAttribute(0, 55)
    feat.setAttribute(1, 'Vasa skola')
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(7476410,5010415)))
    (res, outFeats) = layer.dataProvider().addFeatures([feat])

# 6.4.2. Delete Features
# brisanje featurea po redovima (broji se od 0 do broj manje koji se prikazuje)
if caps and QgsVectorDataProvider.DeleteFeatures:
    res = layer.dataProvider().deleteFeatures([17,18])













