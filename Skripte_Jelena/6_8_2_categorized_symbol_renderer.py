# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#categorized-symbol-renderer

# koristen lejer Osnovne skole na 5km copy

layer = iface.activeLayer()
kategorizovani_renderer = QgsCategorizedSymbolRenderer()

# Dodaje par kategorija
kat1 = QgsRendererCategory('1', QgsMarkerSymbol(), 'kategorija 1')
kat2 = QgsRendererCategory('2', QgsMarkerSymbol(), 'kategorija 2')
kat3 = QgsRendererCategory('3', QgsMarkerSymbol(), 'kategorija 3')

# kreiranje simbola za svaku kategoriju
simbol_1 = QgsMarkerSymbol.createSimple({'name': 'diamond', 'color': 'blue'})
kat1.setSymbol(simbol_1)

simbol_2 = QgsMarkerSymbol.createSimple({'name': 'square', 'color': 'yellow'})
kat2.setSymbol(simbol_2)

simbol_3 = QgsMarkerSymbol.createSimple({'name': 'triangle', 'color': 'orange'})
kat3.setSymbol(simbol_3)

# dodavanje kategorija rendereru
kategorizovani_renderer.addCategory(kat1)
kategorizovani_renderer.addCategory(kat2)
kategorizovani_renderer.addCategory(kat3)

for kat in kategorizovani_renderer.categories():
    print('{}: {} :: {}'.format(kat.value(), kat.label(), kat.symbol()))

kategorizovani_renderer.setClassAttribute('kategorije')
layer.setRenderer(kategorizovani_renderer)
layer.triggerRepaint()
