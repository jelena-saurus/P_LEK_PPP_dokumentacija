# -*- coding: cp1252 -*-
#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/vector.html
#iterating-over-selected-features
#If you only need selected features, you can use the selectedFeatures()
# method from the vector layer:
selection = layer.selectedFeatures()
for feature in selection:
# do whatever you need with the feature
    pass

# Iterating over a subset of features
# vrsi iteraciju nad podskupom feature

layer = iface.activeLayer()

# If you want to iterate over a given subset of features in a layer,
#such as those within a given area, you have to add a
#QgsFeatureRequest object to the getFeatures() call. Here’s an example:
# unutar odredjenog prostora

areaOfInterest = QgsRectangle(7363653,5104094,7598538,4871429)
request = QgsFeatureRequest().setFilterRect(areaOfInterest)

for feature in layer.getFeatures(request):
    if feature[3] < 500.0:
        print('Povrsina opstine je manja od 500 km2')
    else:
        print('Povrsina opstine je veca od 500 km2')

#With setLimit() you can limit the number of
#requested features. Here’s an example:
#moguce je postaviti limit koliko feature-a
#zelimo da bude vraceno
request.setLimit(2)
for feature in layer.getFeatures(request):
    print(feature)
    
#If you need an attribute-based filter instead (or in addition) of a spatial
#one like shown in the examples above, you can build a QgsExpression
#object and pass it to the QgsFeatureRequest constructor. Here’s an example:
# The expression will filter the features where the field "Opstina"
# contains the word "Opovo" (case insensitive)    
# ukoliko zelimo da izvrsimo iteraciju i filtriranje na osnovu
# odredjenog atributa, tu mozemo iskoristimo QgsExpression objekat
# i da ga prosledimo QgsFeatureRequest konstruktoru
exp = QgsExpression('Opstina ILIKE \'%Opovo%\'')
request = QgsFeatureRequest(exp)
for feature in layer.getFeatures(request):
    print(feature[1])

#ili

exp = QgsExpression('povrsina < 500.0')
request = QgsFeatureRequest(exp)
for feature in layer.getFeatures(request):
    print(feature[1])

# Only return selected fields to increase the "speed" of the request
# vraca samo izabrane atribute, kako bi se ubrzao zahtev
x = request.setSubsetOfAttributes([1,6])

# drugi nacin
y = request.setSubsetOfAttributes(['Opstina', 'br_st_02'], layer.fields())

# ne vraca objekte geometrije, kako bi se dodatno ubrzao zahtev
z = request.setFlags(QgsFeatureRequest.NoGeometry)

# vraca samo feature sa specificno navedenim ID
c = request.setFilterFid(67)

# moguce je odredjene opcije povezati i iskoristiti istovremeno
request.setFilterRect(areaOfInterest).setFlags(QgsFeatureRequest.NoGeometry).setFilterFid(2). \
setSubsetOfAttributes([0,6])

for feature in layer.getFeatures(request):
    print("Opstina" +' '+ feature[0] + ' '+"ima povrsinu" +' '+ str(feature[6]))
    
    
    
    
    

    
