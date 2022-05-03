# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#from-an-instance-of-qgsvectorfilewriter

# kreiranje vektora pomocu QgsVectorFileWriter klase

#the QgsVectorFileWriter class: A convenient class for writing vector files to disk,
#using either a static call to writeAsVectorFormatV3() which saves the whole vector
# layer or creating an instance of the class and issue calls to addFeature().
# This class supports all the vector formats that OGR supports
#(GeoPackage, Shapefile, GeoJSON, KML and others).

import os # Ovo je potrebno i u  pyqgis konzoli

# SaveVectorOptions contains many settings for the writer process
# SaveVectorOptions sadrzi brojne funkcionalnosti za snimanje
layer = QgsVectorLayer('point?crs=epsg:6316&field=id:integer', 'point', 'memory')
save_options = QgsVectorFileWriter.SaveVectorOptions()
transform_context = QgsProject.instance().transformContext()

# Pise u GeoPackage format (default)
error = QgsVectorFileWriter.writeAsVectorFormatV2(layer,
                                                  "D:/Jelena/QGIS Projekat/Test_gpkg",
                                                  transform_context,save_options)

if error[0] == QgsVectorFileWriter.NoError:
    print('Uspesno kreiranje lejera.')
else:
    print('Error.')
    
# pise u shapefile formatu (UTF-8 encoding)
layer_shp = QgsVectorLayer('polygon?crs=epsg:6316&field=id:integer', 'polygon', 'memory')
save_options.driverName = 'ESRI Shapefile'
save_options.fileEncoding = 'UTF-8'
error = QgsVectorFileWriter.writeAsVectorFormatV2(layer_shp,
                                                  "D:/Jelena/QGIS Projekat/Test__shp",
                                                  transform_context,save_options)

if error[0] == QgsVectorFileWriter.NoError:
    print('Uspesno kreiranje lejera.')
else:
    print('Error.')
    

# Ucitavanje Test_gpkg lejera sa lokacije

putanja_do_Test_gpkg = 'D:/Jelena/QGIS Projekat/Test_gpkg.gpkg'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_Test_gpkg, 'Test_gpkg', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)

# Ucitavanje Test__shp lejera sa lokacije

putanja_do_Test__shp = 'D:/Jelena/QGIS Projekat/Test__shp.shp'

# Format je:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(putanja_do_Test__shp, 'Test__shp', 'ogr')

# Proverava da li je lejer uspesno ucitan

if not vlayer.isValid():
    print('Lejer nije uspesno ucitan')
else:
    QgsProject.instance().addMapLayer(vlayer)





