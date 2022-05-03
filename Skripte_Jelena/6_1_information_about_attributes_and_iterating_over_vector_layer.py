# You can retrieve information about the fields associated with a vector layer by calling fields()
# on a QgsVectorLayer object
# upotreba vektorskih lejera, vecinom se koristi QgsVectorLayer klasa
#vlayer je vektor

vlayer = QgsVectorLayer('D:/Jelena/QGIS Projekat/Okrug.shp', 'Okrug', 'ogr')
# QgsProject.instance().addMapLayer(vektor) - ukoliko je potrebno da se prikaze na mapi
# izlistava atribute lejera i njihove tipove
for field in vlayer.fields():
    print(field.name(), field.typeName())

#When you load a vector layer, a field is always chosen by QGIS as the Display Name,
# while the HTML Map Tip is empty by default. With these methods you can easily get both
#pozivanje lejera po imenu koje se prikazuje i po imenu
vlayer = QgsVectorLayer('D:/Jelena/QGIS Projekat/Okrug.shp', 'Okrug', 'ogr')
print(vlayer.displayField())


# ovo je najuobicajeniji zahtev - iteracija preko karakteristika u vektorskom sloju
#iterating over the features in a vector layer is one of the most common tasks. Below is an
#example of the simple basic code to perform this task and showing some information about each
#feature. The layer variable is assumed to have a QgsVectorLayer object.
# Get the active layer (must be a vector layer)
# "layer" is a QgsVectorLayer instance

layer = iface.activeLayer()
features = layer.getFeatures()

for feature in features:
    # retrieve every feature with its geometry and attributes
    # vraca svaki feature (tacku, liniju ili poligon tog lejera)
    # zajedno sa njegovom geometrijom i atributima
    print('Feature ID: ', feature.id())
    # fetch geometry
    # show some information about the feature geometry
    geom = feature.geometry()
    geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
    if geom.type() == QgsWkbTypes.PointGeometry:
        # the geometry type can be of single or multi type
        # tip geometrije moze da ima vise tipova
        if geomSingleType:
            x = geom.asPoint()
            print('Tacka: ', x)
        else:
            x = geom.asMultiPoint()
            print('MultiTacka: ', x)
    elif geom.type() == QgsWkbTypes.LineGeometry:
        if geomSingleType:
            x = geom.asPolyline()
            print('Linija: ', x, 'duzina: ', geom.length())
        else:
            x = geom.asMultiPolyline()
            print('MultiLinija: ', x, 'duzina: ', geom.length())
    elif geom.type() == QgsWkbTypes.PolygonGeometry:
        if geomSingleType:
            x = geom.asPolygon()
            print('Poligon: ', x, 'povrsina: ', geom.area())
        else:
            x = geom.asMultiPolygon()
            print('MultiPoligon: ', x, 'povrsina: ', geom.area())
    else:
        print('Geometrija ne postoji ili nije u redu')

    # fetch attributes
    # vraca atribute kao listu, koja sadrzi sve vrednosti tog atributa
    # attrs = atributi (definisanje atributa)
    attrs = feature.attributes()
    print(attrs)
    # for this test only print the first feature
    # prekida se skripta sa break da ne bi izlistao sve atribute, 
    # ukloniti break ukoliko je potrebno da vide sve vrednosti za sve atribute 
     
    break









