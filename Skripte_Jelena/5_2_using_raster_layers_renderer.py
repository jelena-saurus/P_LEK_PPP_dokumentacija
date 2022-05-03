import os
path_to_tif = 'D:/Jelena/QGIS Projekat/NadelEudemSRBLAEA3035.tif'
rlayer = QgsRasterLayer(path_to_tif, 'EudemNadel')
if not rlayer.isValid():
    print('Layer ne moze da se ucita!')
else:
    QgsProject.instance().addMapLayer(rlayer)

#When a raster layer is loaded, it gets a default renderer based on its type.
#It can be altered either in the layer properties or programmatically.

rlayer = QgsProject.instance().mapLayersByName('EudemNadel')[0]

#To query the current renderer
#(postavljanje upita za trenutni renderer)
print(rlayer.renderer())

# To query the current renderer (vraca tip rastera)
print(rlayer.renderer().type())

#To set a renderer, use the setRenderer method of QgsRasterLayer.
#There are a number of renderer classes (derived from QgsRasterRenderer):
#QgsMultiBandColorRenderer
#QgsPalettedRasterRenderer
#QgsSingleBandColorDataRenderer
#QgsSingleBandGrayRenderer
#QgsSingleBandPseudoColorRenderer
#Single band raster layers can be drawn either in gray colors (low values = black,
#high values = white) or with a pseudocolor algorithm that assigns colors to the values.
#Single band rasters with a palette can also be drawn using the palette.
#Multiband layers are typically drawn by mapping the bands to RGB colors.
#Another possibility is to use just one band for drawing.


#Render single band raster layer with colors ranging from green to yellow
#(corresponding to pixel values from 0 to 255).
#(menjanje boje (rendera) za rastere sa jednim kanalom)

# 1 - In the first stage we will prepare a QgsRasterShader object and configure its shader function
# priprema QgsRasterShader object i konfiguracija njegove funkcije sencenja
senka = QgsColorRampShader()
# biranje tipa sencenja
senka.setColorRampType(QgsColorRampShader.Interpolated)
# kreiranje boja koje ce se koristiti (zuta i zelena)
lst = [ QgsColorRampShader.ColorRampItem(0, QColor(0,255,0)),
QgsColorRampShader.ColorRampItem(255, QColor(255,255,0))]
# dodavanje boja sencenju
senka.setColorRampItemList(lst)
# kreiranje shader-a (sencenja)objekta  (objekat QgsColorRampShader)
shader = QgsRasterShader()
shader.setRasterShaderFunction(senka)

# 2 - In the second step we will associate this shader with the raster layer
# povezivanje shader-a sa rasterom
# broj 1 ukazuje broj kanala
renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)
rlayer.setRenderer(renderer)
#Finally we have to use the triggerRepaint method to see the results:
rlayer.triggerRepaint()









