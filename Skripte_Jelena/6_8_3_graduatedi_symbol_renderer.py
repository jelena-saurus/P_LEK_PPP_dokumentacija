# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#graduated-symbol-renderer

# If you wish to create your own graduated symbol renderer you can do so
# as illustrated in the example
# snippet below (which creates a simple two class arrangement)

from qgis.PyQt import QtGui

# koristen lejer Test_simbol
layer = iface.activeLayer()

myVectorLayer = QgsVectorLayer("Test_simbol.shp", "Test_simbol", "ogr")
myTargetField = 'id'
myRangeList = []
myOpacity = 1

# Make our first symbol and range..
# kreira se prvi simbol i opseg
myMin = 0
myMax = 20
myLabel = '0-20'
myColour = QtGui.QColor('#ffee00')
prvi_simbol = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
prvi_simbol.setColor(myColour)
prvi_simbol.setOpacity(myOpacity)
prvi_opseg = QgsRendererRange(myMin, myMax, prvi_simbol, myLabel)
myRangeList.append(prvi_opseg)

# now make another symbol and range
# drugi simbol
myMin = 21
myMax = 33
myLabel = '21-33'
myColour = QtGui.QColor('#00eeff')
drugi_simbol = QgsSymbol.defaultSymbol(myVectorLayer.geometryType())
drugi_simbol.setColor(myColour)
drugi_simbol.setOpacity(myOpacity)
drugi_opseg = QgsRendererRange(myMin, myMax, drugi_simbol, myLabel)
myRangeList.append(drugi_opseg)

renderer = QgsGraduatedSymbolRenderer('', myRangeList)
metod_klasifikacije = QgsApplication.classificationMethodRegistry().method('EqualInterval')
renderer.setClassificationMethod(metod_klasifikacije)
renderer.setClassAttribute(myTargetField)

myVectorLayer.setRenderer(renderer)
myVectorLayer.triggerRepaint()











