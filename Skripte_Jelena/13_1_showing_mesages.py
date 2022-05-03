# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/communicating.html
# showing-messages-the-qgsmessagebar-class

'''Using message boxes can be a bad idea from a user experience point of view.
For showing a small info line or a warning/error messages, the QGIS message bar is usually a better option.'''

# izbacuje poruku u vidu Errora u QGIS-u
iface.messageBar().pushMessage('Error', 'Zao mi je draga, komanda ne moze biti izvrsena', level=Qgis.Critical)
# isti princip, samo sto cetvrti argument definise 
# vreme koliko ce poruka biti prikazana na monitoru
iface.messageBar().pushMessage('Error', 'Zao mi je draga, plugin ne zeli da se pokrene', level=Qgis.Critical, duration=5)

# treci parametar, level, moze se koristiti za kreiranje razlicitih poruka
# koriscenjem Qgis.MessageLevel metode (0:info, 1:warning, 2:error, 3:success)
iface.messageBar().pushMessage('Info', 'Sacuvano je, bez brige', level=Qgis.MessageLevel(0))

def pokaziGresku():
    pass

widget = iface.messageBar().createMessage('Lejeri koji nedostaju', 'Prikazi')
dugme = QPushButton(widget)
dugme.setText('Prikazi')
dugme.pressed.connect(pokaziGresku)
widget.layout().addWidget(dugme)
iface.messageBar().pushWidget(widget, Qgis.Warning)

class Dijalog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.bar = QgsMessageBar()
        self.bar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(50,50,50,50)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Open)
        self.buttonbox.accepted.connect(self.run)
        self.layout().addWidget(self.buttonbox,0,0,2,1)
        self.layout().addWidget(self.bar,0,0,1,1)
    def run(self):
        self.bar.pushMessage('Projekat', 'P_LEK_N_PP', level=Qgis.Info)

dijalog = Dijalog()
dijalog.show()

















