# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# crs.html#crs-transformation 


'''You can do transformation between different spatial reference
systems by using the QgsCoordinateTransform class. The easiest way to use it
is to create a source and destination CRS and construct
a QgsCoordinateTransform instance with them and the current project.
Then just repeatedly call transform() function to do the transformation.
By default it does forward transformation,
but it is capable to do also inverse transformation.'''

# definisanje CRS sistema u toku
crsSrc = QgsCoordinateReferenceSystem('EPSG:6316')

# definisanje zeljenog CRS sistema
# Univerzalni Transferzalni Merkator, zona 34N (odgovara prostoru Srbije)
crsDest = QgsCoordinateReferenceSystem('EPSG:32634')
transformContext = QgsProject.instance().transformContext()
xform = QgsCoordinateTransform(crsSrc, crsDest, transformContext)

tacka1 = xform.transform(QgsPointXY(7436734,5006204))
print('Tacka za transformaciju: ', tacka1)
'''Tacka za transformaciju:  <QgsPointXY: POINT(436319.54619969055056572 5005213.91560371126979589)>
tacka2 = xform.transform(tacka1, QgsCoordinateTransform.ReverseTransform)'''

tacka2 = xform.transform(tacka1, QgsCoordinateTransform.ReverseTransform)
print('Transformisana tacka: ', tacka2)
'''Transformisana tacka:  <QgsPointXY: POINT(7436734.0023883106186986 5006203.99997451063245535)>'''
