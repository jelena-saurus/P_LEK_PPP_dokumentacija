# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# geometry.html#geometry-predicates-and-operations

# QGIS uses GEOS library for advanced geometry operations such as geometry
# predicates (contains(), intersects(), …) and set operations (combine(),
# difference(), …). It can also compute geometric properties of geometries,
# such as area (in the case of polygons) or lengths (for polygons and lines).

# korisceni lejer = Okrug_copy

layer = QgsProject.instance().mapLayersByName('Okrug_copy')[0]
# moze i preko iface.activeLayer()

# filter for `opstine` that begin with `S`, then get their features
# filtrira stene kojima skacenica pocinje sa 'S',
# zatim izvlaci njihove featuree

query = '"Opstina" LIKE \'S%\''
features = layer.getFeatures(QgsFeatureRequest().setFilterExpression(query))

# now loop through the features, perform geometry
# computation and print the results
# vrsi iteraciju nad feature-ima, i izvrsava 
# geometrijsku analizu i stampa rezultate
for f in features:
    geom = f.geometry()
    name = f.attribute('Opstina')
    print(name)
    print('Povrsina (km_2): ', geom.area()/1000000)
    print('Obim (km): ', geom.length())
''' Sopot
```Povrsina (km_2):  273.15959475047197
Obim (km):  80521.10938144692
Savski Venac
Povrsina (km_2):  14.572621654958827
Obim (km):  17479.082082332887
Stari Grad
Povrsina (km_2):  5.344167238787735
Obim (km):  9107.595617050394
Secanj
Povrsina (km_2):  522.3786338103836
Obim (km):  128643.74677858053```'''
   
# Now you have calculated and printed the areas and perimeters of the
# geometries. You may however quickly notice that the values are strange.
# That is because areas and perimeters don’t take CRS into account when
# computed using the area() and length() methods from the QgsGeometry class.
# For a more powerful area and distance calculation, the QgsDistanceArea
# class can be used, which can perform ellipsoid based calculations

# rezultati su neobicni/ neocekivani jer povrsina duzina metode
# za QgsGeometry klasu ne uzimaju u obzir CRS. Za bolje rezultate korisiti se 
#  QgsDistanceArea clasa koja uzima u obzir racunjanje po elipsoidu

# stampa kod od elipsoida koji se koristi
# print(QgsProject.instance().ellipsoid())
# stampa sve elipsoide po njihovom kodu
# print(QgsEllipsoidUtils.acronyms())
query = '"Opstina" LIKE \'S%\''
features = layer.getFeatures(QgsFeatureRequest().setFilterExpression())
d = QgsDistanceArea()
d.setEllipsoid('EPSG:6316')

for f in features:
    geom = f.geometry()
    name = f.attribute('Opstina')
    print(name)
    print('Obim (km): ', d.measurePerimeter(geom)/1000)
    print('Povrsina (km_2): ', d.measureArea(geom)/1000000)
    
''' Surcin
Obim (km):  94.96340889945766
Povrsina (km_2):  289.4709789609375
Sopot
Obim (km):  80.52110938144692
Povrsina (km_2):  273.1595947734375
Savski Venac
Obim (km):  17.479082082332887
Povrsina (km_2):  14.57262165234375
Stari Grad
Obim (km):  9.107595617050395
Povrsina (km_2):  5.34416723828125
Secanj
Obim (km):  128.64374677858052
Povrsina (km_2):  522.3786338164062'''
