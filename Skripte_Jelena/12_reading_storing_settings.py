# -*- coding: cp1252 -*-
# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/settings.html
# reading-and-storing-settings
'''Many times it is useful for a plugin to save some variables so that the
user does not have to enter or select them again next time the plugin is run'''


'''global settings — they are bound to the user at a particular machine. QGIS
itself stores a lot of global settings, for example, main window size or default
snapping tolerance. Settings are handled using the QgsSettings class, through
for example the setValue() and value() methods'''

# cuva podesavanja na globalnom nivou (vezano za korisnika koji koristi
# kompjuter) npr: velicina glavnog prozora..

# sva podesavanja se mogu pregledati sa e 
s = QgsSettings()
#print(s.allKeys())

# skripta za cuvanje radi 
def sacuvaj():
    s = QgsSettings()
    s.setValue("moj_plugin/moj_tekst", "GIS programiranje")
    s.setValue("moj_plugin/moj_celobrojni",  7)
    s.setValue("moj_plugin/moj_realni", 1.61)
    s.setValue("moj_plugin/nepostojeci", None)
    
# skripta za citanje i stampanje ima gresku, ne radi
def procitaj():
    s = QgsSettings()
    moj_tekst = s.value("moj_plugin/moj_tekst", "default text")
    moj_celobrojni  = s.value("moj_plugin/moj_celobrojni", 123)
    moj_realni = s.value("moj_plugin/moj_realni", 2.71)
    nepostojeci = s.value("moj_plugin/nepostojeci", 3.14)
    print(moj_tekst)
    print(moj_celobrojni)
    print(moj_realni)
    print(nepostojeci)
    
projekat = QgsProject.instance()

# cuva vrednosti
projekat.writeEntry("moj_plugin", "moj_tekst", "GIS Prog")
projekat.writeEntry("moj_plugin", "moj_celobrojni", 7)
projekat.writeEntryDouble("moj_plugin", "moj_realni", 1.61)
projekat.writeEntryBool("moj_plugin", "moja_bulova_algebra", True)

  
