# https://docs.qgis.org/3.22/en/docs/
# pyqgis_developer_cookbook/vector.html#adding-and-removing-fields

from qgis.PyQt.QtCore import QVariant 

# koristen lejer = Okrug_copy
layer = iface.activeLayer()
caps = layer.dataProvider().capabilities()

# dodaje atribute izabranom lejeru
if caps and QgsVectorDataProvider.AddAttributes:
    res = layer.dataProvider().addAttributes(
    [QgsField('Opis', QVariant.String),
    QgsField('Povrs_ha', QVariant.Int)])


# alternativne metode za brisanje atributa
lejer.dataProvider().addAttributes([QgsField('f1', QVariant.Int), \
QgsField('f2', QVariant.Int), QgsField('f3', QVariant.Int)])

# azurira dodate/obrisane atribute
lejer.updateFields()       

# stampa atribute koji su trenutno dodeljeni lejeru
for atribut in layer.fields():
    print(atribut.name())
print('--------------------------')
count = layer.fields().count() # vraca broj atributa u lejeru
lista_indeksa = list((count-3, count-2))

# brise jedan atribut pomocu indeksa
layer.dataProvider().deleteAttributes([count-1])

# brise vise atributa pomocu liste sa indeksima
layer.dataProvider().deleteAttributes(lista_indeksa)
layer.updateFields()

for atribut in layer.fields():
    print(atribut.name())


    
