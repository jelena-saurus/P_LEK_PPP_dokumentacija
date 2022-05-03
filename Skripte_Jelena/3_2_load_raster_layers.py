# 3.2 https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/loadlayer.html#raster-layers
#ucitavanje raster lejera (slika)

#potrebno je prvo ucitati sl komandu ne samo u Python Consoli nego i u  pyqgis konzoli

project = QgsProject.instance()

#putanja do rastera u tif formatu na lokaciji D:\Jelena\QGIS Projekat\NadelEudemSRBLAEA3035.tif
#prikazivanje lejera i njegovo imenovanje u EudemNadel
import os
path_to_tif = 'D:/Jelena/QGIS Projekat/NadelEudemSRBLAEA3035.tif'
rlayer = QgsRasterLayer(path_to_tif, 'EudemNadel')
if not rlayer.isValid():
    print('Layer ne moze da se ucita!')
else:
    QgsProject.instance().addMapLayer(rlayer)

# Drugi nacin 
path_to_tif = 'D:/Jelena/QGIS Projekat/NadelEudemSRBLAEA3035.tif'
iface.addRasterLayer(path_to_tif, 'EudemNadel')
