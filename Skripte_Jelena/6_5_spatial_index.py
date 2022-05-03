#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#using-spatial-index

# koriscenje prostornih indeksa

# (Spatial indexes can dramatically improve the performance of your code if you need to do
# frequent queries to a vector layer. Imagine, for instance, that you are writing an interpolation algorithm,
# and that for a given location you need to know the 10 closest points from a points layer, in order to use
# those point for calculating the interpolated value. Without a spatial index, the only way for QGIS to find
# those 10 points is to compute the distance from each and every point to the specified location and then
# compare those distances. This can be a very time consuming task, especially if it needs to be repeated for
# several locations. If a spatial index exists for the layer, the operation is much more effective.
# Think of a layer without a spatial index as a telephone book in which telephone numbers are not ordered or indexed.
# The only way to find the telephone number of a given person is to read from the beginning until you find it.
# Spatial indexes are not created by default for a QGIS vector layer, but you can create them easily.
# This is what you have to do:)

# korisceni lejer = Okrug copy
layer = iface.activeLayer()
feat = QgsFeature(layer.fields())

# reate spatial index using the QgsSpatialIndex class:
# instanciranje objekta koriscenjem klase QgsSpatialIndex
index = QgsSpatialIndex()

# drugi nacin
index.addFeature(feat)

# alternatively, you can load all features of a layer at once using bulk loading
index = QgsSpatialIndex(layer.getFeatures())

# once spatial index is filled with some values, you can do some queries
# returns array of feature IDs of five nearest features
# stampa listu FID-ova 5 najblizih featurea
nearest = index.nearestNeighbor(QgsPointXY(7481447,4971895), 5)
print(nearest)

# returns array of IDs of features which intersect the rectangle
# stampa listu FID-ova featurea koji seku dati pravougaonik
intersect = index.intersects(QgsRectangle(7363653,5104094, 7598538,4871429))
print(intersect)


