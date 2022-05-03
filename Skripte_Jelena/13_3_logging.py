# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/communicating.html
# logging

'''There are three different types of logging available in QGIS to log and
save all the information about the execution of your code.
Each has its specific output location.
- QgsMessageLog is for messages to communicate issues to the use:
- The python built in logging module is for debugging on the level of the QGIS
Python API (PyQGIS). It is recommended for Python script developers
that need to debug their python code, e.g. feature ids or geometries:
- QgsLogger is for messages for QGIS internal debugging / developers.'''

import logging
import os

# izbacuje poruke Log Messages Panelu (donji desni ugao)
# koristi se QgsMessageLog klasa
# korisno za debagovanje 
QgsMessageLog.logMessage('Plugin je uspesno pokrenut', 'Moj_plugin', level=Qgis.Info)
QgsMessageLog.logMessage('Plugin ima znacajnih problema', 'Moj_plugin', level=Qgis.Warning)
QgsMessageLog.logMessage('Plugin je krs', 'Moj_plugin', level=Qgis.Critical)


# koristeci ugradjenu pajtonovu biblioteku: logging

formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
nazivLoga = r'D:/Jelena/QGIS Projekat/proba.log'
logging.basicConfig(filename=nazivLoga, level=logging.DEBUG, format=formatter)
logging.info('Ovaj info ide u fajl.')
logging.debug('Ovaj debug tekst takodje ide u fajl.')


# ukoliko zelimo da izbrisemo log fajl svaki put kada pokrenemo skriptu
if os.path.isfile(nazivLoga):
    with open(nazivLoga, 'w') as file:
        pass
