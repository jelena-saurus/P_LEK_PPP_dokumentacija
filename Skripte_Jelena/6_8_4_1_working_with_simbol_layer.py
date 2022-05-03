# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#working-with-symbol-layers

from qgis.core import QgsSymbolLayerRegistry

#You can get a complete list of the types of symbol layers you can create
# for a given symbol layer class with the following code
# stampa koje sve tipove simbol lejera mozemo da 
# kreiramo za datu klasu simbola
# klasa QgsSymbolLayerRegistry upravlja bazom podataka
# u kojoj se nalaze svi moguci tipovi simbola
myRegistry = QgsApplication.symbolLayerRegistry()
myMetadata = myRegistry.symbolLayerMetadata('SimpleFill')
for item in myRegistry.symbolLayersForType(QgsSymbol.Marker):
    print(item)

#EllipseMarker
#FilledMarker
#FontMarker
#GeometryGenerator
#MaskMarker
#RasterMarker
#SimpleMarker
#SvgMarker
#VectorField


