# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#appearance-symbology-of-vector-layers

#When a vector layer is being rendered, the appearance of the data is given by
# renderer and symbols associated with the layer. Symbols are classes which take
# care of drawing of visual representation of features,
# while renderers determine what symbol will be used for a particular feature


# koristen lejer - ceni lejer: Osnovne skole na 5km copy
layer = iface.activeLayer()

#The renderer for a given layer can be obtained as shown below
#iscitava tip prikaza lejera (single Symbol, CategorizedSymbol, GraduatedSymbol)
renderer = layer.renderer()

print('Tip: ', renderer.type())

# It is possible to obtain a dump of a renderer contents in text form —
# can be useful for debugging
print(renderer.dump())

# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#single-symbol-renderer

# menja simbol lejera
simbol = QgsMarkerSymbol.createSimple({'name': 'triangle', 'color': 'lightgreen'})
renderer.setSymbol(simbol)
layer.triggerRepaint()

# ukoliko zelimo da vidimo sve osobenosti 
# prvog simbol lejera koji smo kreirali 
print(renderer.symbol().symbolLayers()[0].properties())

# menja velicinu simbola
renderer.symbol().symbolLayer(0).setSize(3)
# nekim osobenostima nije moguce pristupiti pomocu metoda,
# vec se moze zameniti simbol u potpunosti
props = layer.renderer().symbol().symbolLayer(0).properties()
props['name'] = 'square'
props['color'] = 'red'
renderer.setSymbol(QgsMarkerSymbol.createSimple(props))
# prikazuje promene
layer.triggerRepaint()

