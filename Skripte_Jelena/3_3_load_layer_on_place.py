#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/loadlayer.html#qgsproject-instance
#ucitavanje i postavljanje lejera na tacnu poziciju u okviru stabla prikazanih lejera qGis projekta
#primer. ucitavanja i spustanje rastera na poslednju poziciju da ne bi njegov prikaz blokirao pogled na tackaste i poligon lejere)

path_to_tif = 'D:/Jelena/QGIS Projekat/NadelEudemSRBLAEA3035.tif'
rlayer = QgsRasterLayer(path_to_tif, 'EudemNadel')

# Prvo se dodaje lejer, bez "pokazivanja"
QgsProject.instance().addMapLayer(rlayer, False)

# Pristupa se "stablu" lejera koji je na vrhu projekta
layerTree = iface.layerTreeCanvasBridge().rootGroup()

# Pozicija se definise kao prvi argument (-1, za poslednje mesto)
layerTree.insertChildNode(-1, QgsLayerTreeLayer(rlayer))


# Ukoliko zelimo da uklonimo lejer
# QgsProject.instance().removeMapLayer(rlayer.id())

# Ukoliko zelimo da izlistamo ucitana lejere i njihove ID-e
# QgsProject.instance().mapLayers()
