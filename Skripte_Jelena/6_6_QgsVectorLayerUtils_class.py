# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#the-qgsvectorlayerutils-class

# The QgsVectorLayerUtils class contains some very useful methods
# that you can use with vector layers. For example the createFeature()
# method prepares a QgsFeature to be added to a vector layer keeping all
# the eventual constraints and default values of each field:
# createFeature() metoda priprema QgsFeature objekat da bude dodat lejeru
# zadrzavajuci sva ogranicenja i default vrednosti
# koristeni lejer Okrug copy.shp i atribut Opis

vlayer = QgsVectorLayer("Okrug copy.shp", "Opis", "ogr")
feat = QgsVectorLayerUtils.createFeature(vlayer)

# The getValues() method allows you to quickly get the values of a field or expression:
# getValues metod omogucava dobijanje vrednosti
# za odredjeni atribut ili izraz
vlayer.selectByIds([0])
value = QgsVectorLayerUtils.getValues(vlayer, 'Opis', selectedOnly=True)
print(value)
