# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/communicating.html
# showing-progress

import time

'''from qgis.PyQt.QtWidgets import QProgressBar
from qgis.PyQt.QtCore import *'''


napredakPoruka = iface.messageBar().createMessage('Strpi se, samo da zavrsim...')
napredak = QProgressBar()
napredak.setMaximum(5)
napredak.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
napredakPoruka.layout().addWidget(napredak)
iface.messageBar().pushWidget(napredakPoruka, Qgis.Info)

for i in range(5):
    time.sleep(1)
    napredak.setValue(i + 1)


# za prekidanje rada widgeta
# iface.messageBar().clearWidgets()



