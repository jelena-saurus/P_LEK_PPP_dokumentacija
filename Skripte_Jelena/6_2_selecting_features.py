#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
#vector.html#selecting-features

# Get the active layer (must be a vector layer)
# Potrebno obeleziti lejer u legendi, mora da bude vektor
layer = iface.activeLayer()
# Selektuje sve feature lejera
layer.selectAll()

# select using an expression, use the selectByExpression() method:
# Assumes that the active layer is Okrug.shp file from the QGIS test suite
# U Okrug.shp su atributi Opstina (string), ID1 (number), Okrug (string), povrsina (number),
# opstina_la (string), br_st_2002 (number), gus_nas_02 (number), op_la (number)
# Selektuje feature na osnovu odredjenog izraza
# funkcija za selekciju se sastoji od dva argumenta. prvi argument predstavlja izraz, na osnovu kog se vrsi upit
layer.selectByExpression('"br_st_2002" > 25000 and "gus_nas_02" > 55 and "gus_nas_02" < 155', QgsVectorLayer.SetSelection)

#To change the selection color you can use setSelectionColor() method of QgsMapCanvas as shown in the following example
#menja boju selekcije (default je zuta)
iface.mapCanvas().setSelectionColor(QColor('red'))

# featurima u okviru atributa (kolona atributne tabele) se moze pristupiti na osnovu imena ili indeksa
print(feature['Opstina'])
print(feature[5])

# ukoliko su nam potrebni samo selektovani feature-i
select = layer.selectedFeatures()
for feature in select:
    if feature['br_st_2002'] < 25000:
        print('Broj stanovnika je manji od 250000')
    else:
        print('Broj stanovnika je veca od 250000')



# clear the selection
# brise selekciju 
layer.removeSelection()
















