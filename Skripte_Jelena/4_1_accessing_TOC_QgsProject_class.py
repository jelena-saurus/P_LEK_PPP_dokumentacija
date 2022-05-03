#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/legend.html
#Accessing the Table Of Contents (TOC)/legend widget / legendom (sinonimi)
#You can use different classes to access all the loaded layers in the TOC and use them to retrieve information:
# QgsProject or
# QgsLayerTreeGroup

#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/legend.html#id1
#You can use QgsProject to retrieve information about the TOC and all the layers loaded.
#You have to create an instance of QgsProject and use its methods to get the loaded layers.
#The main method is mapLayers(). It will return a dictionary of the loaded layers

# stampanje liste lejera

layers = QgsProject.instance().mapLayers()
print(layers)


# The dictionary keys are the unique layer ids while the values are the related objects.
# It is now straightforward to obtain any other information about the layers
# daje listu lejera pomocu komprhenzije liste

# list of layer names using list comprehension
l = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
# dictionary with key = layer name and value = layer object
layers_list = {}
for l in QgsProject.instance().mapLayers().values():
  layers_list[l.name()] = l

print(layers_list)

#REZULTAT
{'Granica Okruga': <QgsVectorLayer: 'Granica Okruga' (ogr)>,
'NadelGKZ': <QgsVectorLayer: 'NadelGKZ' (ogr)>,
'Okrug': <QgsVectorLayer: 'Okrug' (ogr)>,
'Osnovne skole na 5km': <QgsVectorLayer: 'Osnovne skole na 5km' (ogr)>,
'pesacka distanca 5km': <QgsVectorLayer: 'pesacka distanca 5km' (ogr)>}

# Moguce je izvrsiti selekciju lejera pomocu njegovog imena
# You can also query the Table Of Contents (TOC)using the name of the layer

Granica = QgsProject.instance().mapLayersByName('Granica Okruga')[0]
print(Granica.name())

# list with all the matching layers is returned, so we index with [0] to get the first layer with this name
# [0] se stavlja da bi se odstampalo prvi lejer sa tim imenom
