# -*- coding: cp1252 -*-
#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/composer.html
#output-using-print-layout


import os

project = QgsProject.instance()
layout = QgsPrintLayout(project)
layout.initializeDefaults()

# adding an empty A4 page to the layout. You can create layouts without calling
# the initializeDefaults() method,
# but you’ll need to take care of adding pages to the layout yourself
# ukoliko kreiramo novi layout(dizajn) za stampanje, korisno je izvrsiti 
# inicijalizaciju default podesavanja, cime kreiramo prazan A4 list
# This initializes the layout with some default settings, specifically by

layout.setName('MyLayout')
project.layoutManager().addLayout(layout)

# Now we can add various elements (map, label, …) to the layout.
# All these objects are represented by classes that inherit from the base
# QgsLayoutItem class

# kreiranje mape
map = QgsLayoutItemMap(layout)
# # Set map item position and size (by default,
# it is a 0 width/0 height item placed at 0,0)
# Podesava poziciju i velicinu mape (default vrednosti su 
# 0 za sirinu i visinu i postavljena je na 0,0)
map.attemptMove(QgsLayoutPoint(5,5, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(200,200, QgsUnitTypes.LayoutMillimeters))
# Definise obim koji ce se renderovati
map.zoomToExtent(iface.mapCanvas().extent())
layout.addLayoutItem(map)

# kreiranje labela
label = QgsLayoutItemLabel(layout)
label.setText("Hello world")
label.adjustSizeToText()
layout.addLayoutItem(label)

# kreiranje legende
legend = QgsLayoutItemLegend(layout)
legend.setLinkedMap(map) # map is an instance of QgsLayoutItemMap
layout.addLayoutItem(legend)

# kreiranje razmernika
item = QgsLayoutItemScaleBar(layout)
item.setStyle('Numeric') # optionally modify the style
item.setLinkedMap(map) # map is an instance of QgsLayoutItemMap
item.applyDefaultSize()
layout.addLayoutItem(item)

# Once an item is added to the layout, it can be moved and resized:
label.attemptMove(QgsLayoutPoint(150,1.5, QgsUnitTypes.LayoutMillimeters))
legenda.attemptMove(QgsLayoutPoint(250, 5, QgsUnitTypes.LayoutMillimeters))
razmernik.attemptMove(QgsLayoutPoint(60, 190, QgsUnitTypes.LayoutMillimeters))

# skripta ne radi sve, ne renderuje mapu
# razmernika, oznaku za sever


# exportovanje karte u PDF formatu
base_path = os.path.join(QgsProject.instance().homePath())
pdf_path = os.path.join(base_path, 'izlaz.pdf')

exporter = QgsLayoutExporter(layout)
exporter.exportToPdf(pdf_path, QgsLayoutExporter.PdfExportSettings())















