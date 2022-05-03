# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
#vector.html#from-an-instance-of-qgsvectorlayer

# kreiranje privremenih lejera - u memoriji, ne ucitavaju se u qgis okruzenju i ne upisuju se na disk

# Among all the data providers supported by the QgsVectorLayer class,
# let’s focus on the memory-based layers. Memory provider is intended to be used
# mainly by plugin or 3rd party app developers. It does not store data on disk,
# allowing developers to use it as a fast backend for some temporary layers.

# kreira se lejer 
layer = QgsVectorLayer('Tacke', 'privremene_tacke', 'memory')
priv = layer.dataProvider()

# dodavanje atributa
priv.addAttributes(
[QgsField('naziv', QVariant.String),
QgsField('mesto', QVariant.Int),
QgsField('velicina', QVariant.Double)]
)

layer.updateFields() # obavestava vektorski lejer da azurira promene od provajdera

# dodavanje feature-a
feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(7367413,4940679)))
feat.setAttributes(['Tip', 2, 0.3])
priv.addFeatures([feat])

# azurira obim lejera kada su dodati novi feature-i
# posto se promena obima provajdera ne odrazava direktno na lejer
layer.updateExtents 

print('fields: ', len(priv.fields()))
print('features: ', priv.featureCount())
e = layer.extent()
print('obim: ', e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())

# vrsi iteraciju nad feature-ima
features = layer.getFeatures()
for feat in features:
    print('F: ', feat.id(), feat.attributes(), feat.geometry().asPoint())





