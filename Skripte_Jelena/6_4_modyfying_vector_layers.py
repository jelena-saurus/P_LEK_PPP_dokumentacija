# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#modifying-vector-layers
# korisceni lejer: Okrug_copy
layer = iface.activeLayer()

# proverava da li je odredjena funkcija podrzana
caps = layer.dataProvider().capabilities()

if caps and QgsVectorDataProvider.AddAttributes:
    print('Lejer podrzava dodavanje atributa!')

# Proverava sve moguce funkcije lejera    
caps_string = layer.dataProvider().capabilitiesString()
print(caps_string)


# dodavanje featurea
if caps and QgsVectorDataProvider.AddFeatures:
    feat = QgsFeature(layer.fields())
    feat.setAttribute(0, 3)
    feat.setAttribute(1, 'Stablo bukve')
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(7362596,4940331)))
    (res, outFeats) = lejer.dataProvider().addFeatures([feat])

# brisanje featurea
#if caps and QgsVectorDataProvider.DeleteFeatures:
    #res = lejer.dataProvider().deleteFeatures([2,3])
# res

# Menjanje featurea (geometrije ili atributa)
# obratiti paznju na to koji je FID od featurea
#fid = 3 - postoji mogucnost da je doslo do promene FIDa

#if caps and QgsVectorDataProvider.ChangeAttributeValues:
    #atributi = {0 : 4, 1: 'Stablo breze'}
    #lejer.dataProvider().changeAttributeValues({fid : atributi})











