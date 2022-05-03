# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/
# crs.html#coordinate-reference-systems

'''QGIS supports different CRS identifiers with the following formats:
EPSG:<code> — ID assigned by the EPSG organization - handled with createFromOgcWms()
POSTGIS:<srid>— ID used in PostGIS databases - handled with createFromSrid()
INTERNAL:<srsid> — ID used in the internal QGIS database - handled with createFromSrsId()
PROJ:<proj> - handled with createFromProj()
WKT:<wkt> - handled with createFromWkt()'''

# proveravam primer sa WGS 84 EPSG 4326 i on je ispravan
# specify CRS by its ID - na primer EPSG 4326 for WGS84
crs = QgsCoordinateReferenceSystem('EPSG:4326')
# stampa 
print(crs.isValid())

# specify CRS by its well-known text (WKT)
wkt = 'GEOGCS["WGS84", DATUM["WGS84", SPHEROID["WGS84", 6378137.0, 298.257223563]],' \
      'PRIMEM["Greenwich", 0.0], UNIT["degree",0.017453292519943295],' \
      'AXIS["Longitude",EAST], AXIS["Latitude",NORTH]]'
crs = QgsCoordinateReferenceSystem(wkt)
print(crs.isValid())


# pravim prilagodjeni wkt na osnovu primera za WGS 84 EPSG 4326 i radim na nasem referentnom sistemu MGI 1901/ Balkans zone 7
# menjam ponovo referentni sistem u MGI 1901 /Balkans zone 7
# specify CRS by its ID - na primer EPSG 6316 is allocated for MGI 1901/ Balkans zone 7
crs = QgsCoordinateReferenceSystem('EPSG:6316')
# stampa 
print(crs.isValid())

# specify CRS by its well-known text (WKT) 
wkt = 'GEOGCS["MGI 1901", DATUM["WGS84", ELLIPSOID["Bessel 1841", 6377397.155,299.1528128]],' \
      'PRIMEM["Greenwich", 0.0], UNIT["degree",0.0174532925199433],' \
      'AXIS["Longitude",EAST], AXIS["Latitude",NORTH]]'
crs = QgsCoordinateReferenceSystem(wkt)
print(crs.isValid())

# Opis MGI 1901 / Balkans zone 7 iy=z Qgis-a. Uzimamo samo proj 4. 
''' WKT
PROJCRS["MGI 1901 / Balkans zone 7",
    BASEGEOGCRS["MGI 1901",
        DATUM["MGI 1901",
            ELLIPSOID["Bessel 1841",6377397.155,299.1528128,
                LENGTHUNIT["metre",1]]],
        PRIMEM["Greenwich",0,
            ANGLEUNIT["degree",0.0174532925199433]],
        ID["EPSG",3906]],
    CONVERSION["Balkans zone 7",
        METHOD["Transverse Mercator",
            ID["EPSG",9807]],
        PARAMETER["Latitude of natural origin",0,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8801]],
        PARAMETER["Longitude of natural origin",21,
            ANGLEUNIT["degree",0.0174532925199433],
            ID["EPSG",8802]],
        PARAMETER["Scale factor at natural origin",0.9999,
            SCALEUNIT["unity",1],
            ID["EPSG",8805]],
        PARAMETER["False easting",7500000,
            LENGTHUNIT["metre",1],
            ID["EPSG",8806]],
        PARAMETER["False northing",0,
            LENGTHUNIT["metre",1],
            ID["EPSG",8807]]],
    CS[Cartesian,2],
        AXIS["easting (Y)",east,
            ORDER[1],
            LENGTHUNIT["metre",1]],
        AXIS["northing (X)",north,
            ORDER[2],
            LENGTHUNIT["metre",1]],
    USAGE[
        SCOPE["unknown"],
        AREA["Europe - former Yugoslavia onshore 19.5°E to 22.5°E"],
        BBOX[40.85,19.5,46.19,22.51]],
    ID["EPSG",6316]]
Proj4
+proj=tmerc +lat_0=0 +lon_0=21 +k=0.9999 +x_0=7500000 +y_0=0 +ellps=bessel +towgs84=682,-203,480,0,0,0,0 +units=m +no_defs
Extent
19.50, 40.85, 22.51, 46.19 '''

# komande za pristup specificnim informacijama o koordinatnom sistemu

print('QGIS CRS ID: ', crs.srsid())
print('PostGIS SRID: ', crs.postgisSrid())
print('Opis: ', crs.description())
print('Akronim projekcije: ', crs.projectionAcronym())
print('Akronim elipsoida: ', crs.ellipsoidAcronym())
print('Proj String: ', crs.toProj4())

# proverava da li je geografski ili projektovani koordinatni sistemi
print('Da li je geografski: ', crs.isGeographic())

# proverava mernu jedinicu za korisceni koordinatni sistem
print('Merna jedinica mape: ', crs.mapUnits())









