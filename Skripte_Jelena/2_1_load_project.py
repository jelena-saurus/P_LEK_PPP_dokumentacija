#2 https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/loadproject.html

# Instanciranje projekta - ova komada je data kao prva pripremna komanda ali je preduslov
# komandi ucitavanja projekta pa je ponavljam 
project = QgsProject.instance()

# 2_1_Ucitavanje projekta
project.read('D:/Jelena/QGIS Projekat/Projekat.qgz')

