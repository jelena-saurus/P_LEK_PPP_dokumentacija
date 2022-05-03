# -*- coding: utf-8 -*-
#A raster layer consists of one or more raster bands — referred to as single band and multi band rasters.
#One band represents a matrix of values. A color image (e.g. aerial photo) is a raster consisting of red,
#blue and green bands. Single band rasters typically represent either continuous variables (e.g. elevation)
#or discrete variables (e.g. land use). In some cases, a raster layer comes with a palette
#and the raster values refer to the colors stored in the palette.
#The following code assumes rlayer is a QgsRasterLayer object.

rlayer = QgsProject.instance().mapLayersByName('NadelEudemSRBLAEA3035.tif')[0]
# get the resolution of the raster in layer unit (vraca rezoluciju lejera)
print(rlayer.width(), rlayer.height())

# get the extent of the layer as QgsRectangle (vraća prostiranje lejera)
print(rlayer.extent())

# get the extent of the layer as Strings(vraca x i y koordinate rastera kao stringove)
print(rlayer.extent().toString())

# get the raster type: 0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband
# (vraca tip raster: 0 = grayscale (1 kanal), 1 = paleta (1 kanal), 2 = vise kanala (multiband))
print(rlayer.rasterType())

# get the total band count of the raster
#(vraca broj kanala od rastera (za multispektralne snimke bi bilo vise))
print(raster.bandCount())

# vraca naziv prvog spektralnog kanala od rastera
print(raster.bandName(1))

# get all the available metadata as a QgsLayerMetadata object
# vraca metapodatke od rastera kao QgsLayerMetadata objekat
print(raster.metadata())
















