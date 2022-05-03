#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/legend.html
#Accessing the Table Of Contents (TOC)/ legend widget / legendom (sinonimi)
#You can use different classes to access all the loaded layers in the TOC and use them to retrieve information:
# QgsProject or
# QgsLayerTreeGroup


#https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/legend.html#qgslayertreegroup-class
#The layer tree is a classical tree structure built of nodes.
#There are currently two types of nodes: group nodes (QgsLayerTreeGroup) and layer nodes (QgsLayerTreeLayer).

# Pristupanje Table Of Contents (TOC)/ legend widget / legendi i manipulisanje lejerima u njoj
# Instanciranje root-a (pocetnog cvora) Table Of Contents (TOC)/ legend widget / legende

root = QgsProject.instance().layerTreeRoot()

# root je grupni cvor u okviru koga su poredjani lejeri ("deca")

root.children()

#We can retrieve one of the children:
dete0 = root.children()[0]
print(dete0)

# Lejerima se takodje moze pristupiti pomocu unikatnog ID-ja
ids = root.findLayerIds()
root.findLayer(ids[0])


# Lejerima se takodje moze pristupiti pomocu unikatnog ID-ja i odstampati
ids = root.findLayerIds()
x = root.findLayer(ids[0])
print(x)

# Izbacuje listu svih lejera koji su "ukljuceni"
ukljuceni_lejeri = root.checkedLayers()
print(ukljuceni_lejeri)

#Postoje dva nacina za dodavanje lejera u stablu Table Of Contents (TOC)/ legend widget / legende
# 1. explicitno dodavanje - kreiranje "privremeni" lejer
layer1 = QgsVectorLayer('D:/Jelena/QGIS Projekat/priv_lejer', 'privremeni', 'memory')

# dodavanje keriranog privremeog lejera na poslednju poziciju u legendi
root.addLayer(layer1)

# dodaje lejer na specificno navedenu poziciju
#root.insertLayer(3, layer1)

# 2. implicitno dodavanje lejera u registar lejera mape kada je stablo lejera povezano sa registrom lejera
# QgsProject.instance()addMapLayer(layer1)

# dodavanje grupa
node_group1 = root.addGroup('Grupa')
# dodaje podgrupu prethodno kreiranoj grupi
node_subgroup1 = node_group1.addGroup('Podgrupa')

# Takodje, grupe isto mogu da se pretrazuju pomocu naziva
root.findGroup('Grupa')

# Prebacivanje cvorova i grupa
# prvo se klonira postojeci cvor grupe
cloned_group1 = node_group1.clone()
# zatim se pomera cvor (ujedno se pomeraju i lejeri i podgrupe)na vrh
root.insertChildNode(0, cloned_group1)
# uklanjanje originalnog cvora
root.removeChildNode(node_group1)

root = QgsProject.instance().layerTreeRoot()
granica = QgsProject.instance().mapLayersByName('Granica Okruga')[0]


# pomeranje lejera u legendi
# kreiranje objekta QgsLayerTreeLayer iz lejera granica po njegovom ID-u
granicavektor = root.findLayer(granica.id())
# klonira se prethodno kreirani objekat
granicavektorklon = granicavektor.clone()
# uzima "roditelja". Ukoliko je rezultat None,
# znaci da lejer nije ni u jednog grupi i vratice ''
roditelj = granicavektor.parent()
# pomera se klonirani lejer na vrh
roditelj.insertChildNode(0, granicavektorklon)
# uklanja se originalni lejer (granicavektor)
root.removeChildNode(granicavektor)

# prebacivanje lejera u odredjenu grupu (slican postupak kao kod pomeranja)
granicavektor = root.findLayer(granica.id())
granicavektorklon = granicavektor.clone()
# kreiranje nove grupe u okviru koje se pomera 
grupa1 = root.addGroup('Grupa')
roditelj = granicavektor.parent()
grupa1.insertChildNode(0, granicavektorklon)
roditelj.removeChildNode(granicavektor)

# jos neke metode, koje mogu da se koriste za menjanje
# grupa i lejera

# menjanje imena grupe
# node_group1.setName('Granice')

# menjanje naziva lejera
#node_layer2 = root.findLayer(granica.id())
#print(node_layer2.name())
#node_layer2.setName('Granica_Okruga_Nadel')
#print(node_layer2.name())

# ukljucivanje i iskljucivanje lejera
#node_group1.setItemVisibilityChecked(True)
#node_layer2.setItemVisibilityChecked(False)

# prosiruje i sakriva grupe u legendi
#node_group1.setExpanded(True)
#node_group1.SetExpanded(False)


