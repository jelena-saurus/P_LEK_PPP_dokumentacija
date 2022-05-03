# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# vector.html#directly-from-features

# define fields for feature attributes. A QgsFields object is needed
# definise polja (fields) za atribute feature. Neophodno istancirati QgsFields()
fields = QgsFields()
fields.append(QgsField('prvi', QVariant.Int))
fields.append(QgsField('drugi', QVariant.String))

# create an instance of vector file writer, which will create the vector file.
# kreira instancu vektor file writer-a , koji ce kreirati vektorski fajl
# Arguments: 
# 1. path to new file (will fail if exists already)
# 2. field map
# 3. geometry type - from WKBTYPE enum
# 4. layer's spatial reference (instance of QgsCoordinateReferenceSystem)
# 5. coordinate transform context
# 6. save options (driver name for the output file, encoding etc.)


crs = QgsProject.instance().crs()
transform_context = QgsProject().instance().transformContext()
save_options = QgsVectorFileWriter.SaveVectorOptions()
save_options.driverName = 'ESRI Shapefile'
save_options.fileEncoding = 'UTF-8'

writer = QgsVectorFileWriter.create(
'D:/Jelena/QGIS Projekat/Test__from_feature', fields, QgsWkbTypes.Point, crs,
transform_context, save_options)

if writer.hasError() != QgsVectorFileWriter.NoError:
    print('Greska pri kreiranju lejera: ', writer.errorMessage())

#lejer je napravljen ali nije hteo da se ucita. dodavanje takodje nije uspelo.  



