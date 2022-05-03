# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#modifying-vector-layers-with-an-editing-buffer
# Favor QgsVectorLayerEditUtils class for geometry-only edits
# If you only need to change geometries, you might consider using
# the QgsVectorLayerEditUtils which provides some
# useful methods to edit geometries (translate, insert or move vertex, etc.).

# koristen lejer - Osnovne skole na 5km copy

# To start the editing mode, use the startEditing() method
# leyer je staviti u mod za editovanje 
layer = iface.activeLayer()
layer.startEditing()

#potebno je proveriti da li je lejer moze ili ne da se menja (edituje)
print(layer.isEditable())

# dodavanje dva nova featurea
from qgis.PyQt.QtCore import QVariant
feat1 = feat2 = QgsFeature(layer.fields())
fid = 18 # 
feat1.setId(fid)

# add two features (QgsFeature instances)
# dodaje dva featurea (instance QgsFeature)
layer.addFeatures([feat1,feat2])

# delete a feature with specified ID
# brise feature sa prethodno definisanim FID-om
layer.deleteFeature(fid)

# set new geometry (QgsGeometry instance) for a feature
# postavlja novu geometriju (instanca QgsGeometry) za feature
# moze se takodje koristiti QgsGeometry.fromPointXY(QgsPointXY(koordinate))
geom = QgsGeometry.fromWkt('POINT(7481447 4971895)')
layer.changeGeometry(fid, geom)

# update an attribute with given field index (int) to a given value
# azurira atribut preko indeksa tog atributa
# za odredjenu vrednost
fieldIndex = 1
value = 'skola'
layer.changeAttributeValue(fid, fieldIndex, value)

# ukoliko zelimo da dodamo atribut
layer.addAttribute(QgsField('od_Nadela', QVariant.Int))

# add new field
layer.addAttribute(QgsField("mytext", QVariant.String))

# remove a field
# ukoliko zelimo da obrisemo atribut
layer.deleteAttribute(fieldIndex)

# izlezenje iz edit moda
layer.commitChanges()
#false
# Returns the result of the attempt. If a commit fails (i.e. False is returned),
# the in-memory changes are left untouched and are not discarded. This allows editing
# to continue if the commit failed on e.g. # a disallowed value in a
# Postgres database - the user can re-edit and try again.

