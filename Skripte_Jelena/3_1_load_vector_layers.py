# -*- coding: cp1252 -*-
#3.1 https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/loadlayer.html#vector-layers

#potrebno i ukolko se radi na konzoli pythona u okviru QGIS-u

import os 

# Ucitavanje 1. lejera sa lokacije

putanja_do_Granica_Okruga = 'D:/Jelena/QGIS Projekat/Granica Okruga.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_Granica_Okruga, 'Granica Okruga', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)

# Ucitavanje 2. lejera sa lokacije

putanja_do_Okrug = 'D:/Jelena/QGIS Projekat/Okrug.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_Okrug, 'Okrug', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)

# Ucitavanje 3. lejera sa lokacije
#NAPOMENA - ovaj lejer je vracao gresku da nije dobro definisan naziv, naziv je prvo skracen sa Nadel_osovina_reke na Nadel,
#sto nije dalo rezultat, pa mu je posle promene projekcije,
#prethodno je lejer bio u EPSG 4326 kao i lejer Osnovne skole na 5km koji je uspesno ucitan, prebacen je kao vecina lejera u GKZ7
#i promenjen mu je dodatno naziv u NadelGKZ bez rezultata
#okrenuti su sleševi - to je nije vracalo gresku ali nije ni ucitan lejer
#otkrivena je greška u pisanju komade - nije data dobra putanja

putanja_do_NadelGKZ = 'D:/Jelena/QGIS Projekat/NadelGKZ.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_NadelGKZ, 'NadelGKZ', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)

# Ucitavanje 4. lejera sa lokacije

putanja_do_Osnovne_skole_na_5km = 'D:/Jelena/QGIS Projekat/Osnovne skole na 5km.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_Osnovne_skole_na_5km, 'Osnovne skole na 5km', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)

# Ucitavanje 5. lejera sa lokacije

putanja_do_pesacka_distanca_5km = 'D:/Jelena/QGIS Projekat/pesacka distanca 5km.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_pesacka_distanca_5km, 'pesacka distanca 5km', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)


