# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#working-with-symbols

# For representation of symbols, there is QgsSymbol base class with three derived classes:
# QgsMarkerSymbol — for point features
# QgsLineSymbol — for line features
# QgsFillSymbol — for polygon features

# Every symbol consists of one or more symbol layers (classes derived from QgsSymbolLayer).
# The symbol layers do the actual rendering,
# the symbol class itself serves only as a container for the symbol layers.

marker_symbol = QgsMarkerSymbol()
for i in range(marker_symbol.symbolLayerCount()):
    lyr = marker_symbol.symbolLayer(i)
    print("{}: {}".format(i, lyr.layerType()))

# stampa koje sve tipove simbol lejera mozemo da 
# kreiramo za datu klasu simbola
# klasa QgsSymbolLayerRegistry upravlja bazom podataka
# u kojoj se nalaze svi moguci tipovi simbola
registar = QgsApplication.symbolLayerRegistry()
metapodaci = registar.symbolLayerMetadata('SimpleFill')
for item in registar.symbolLayersForType(QgsSymbol.Marker):
    print(item)

simbol = QgsMarkerSymbol()
simbol.properties()
