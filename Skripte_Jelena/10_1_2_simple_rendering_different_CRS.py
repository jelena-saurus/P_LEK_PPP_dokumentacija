# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/composer.html
#map-rendering-and-printing

# uzima odredjeni lejer i na osnovu njega kreira sliku

import os

lokacija_slike = os.path.join(QgsProject.instance().homePath(), 'D:/Jelena/QGIS Projekat/PPPancevo.png')

layer = QgsProject.instance().mapLayersByName('Okrug_copy')[0]
settings = QgsMapSettings()
settings.setLayers([layer])
settings.setBackgroundColor(QColor(255, 255, 255))
settings.setOutputSize(QSize(800, 600))
settings.setExtent(layer.extent())

render = QgsMapRendererParallelJob(settings)

def zavrsen():
    slika = render.renderedImage()
    # cuvanje slike
    slika.save(lokacija_slike, 'png')

render.finished.connect(zavrsen)
# daje kao odgovor PyQt5.QtCore.QMetaObject.Connection object at 0x000001E604333D68

# Zapocinje renderovanje
render.start()
# daje odgovor PyQt5.QtCore.QMetaObject.Connection object at 0x000001E604313208

# ukoliko je standalone skripta, neophodno je importovati ovaj modul
# zbog specificne petlje (posto je ova skripta pisana da se pokrece
# unutar samog QGIS-a, nema potrebe da se importuje)
# from qgis.PyQt5.QtCore import QEventLoop
petlja = QEventLoop()
render.finished.connect(petlja.quit)
petlja.exec_()

# daje odgovor -1
# ?


# ukoliko imamo vise razlicitih lejera, u razlicitim koordinatnim sistemima
# neophodno je da namestimo koordinatni sistem u kom zelimo da lejer bude prikazan
# lejeri = [iface.activeLayer()]
# settings.setLayers(lejeri)
# settings.setDestinationCrs(lejeri[0].crs())








