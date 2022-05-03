# https://docs.qgis.org/3.22/en/docs/pyqgis_developer_cookbook/tasks.html
# introduction

'''Background processing using threads is a way to maintain a responsive user
interface when heavy processing is going on. Tasks can be used to achieve threadin
g in QGIS.
A task (QgsTask) is a container for the code to be performed in the background,
and the task manager (QgsTaskManager) is used to control the running of the task
s. These classes simplify background processing in QGIS by providing mechanisms
for signaling, progress reporting and access to the status for background proces
ses. Tasks can be grouped using subtasks.
The global task manager (found with QgsApplication.taskManager()) is normally
used. This means that your tasks may not be the only tasks
that are controlled by the task manager.'''

# There are several ways to create a QGIS task:
# nacini na koje se sve moze kreirati task

#Create your own task by extending QgsTask
# pomocu klase QgsTask
class PosebanTask(QgsTask):
    pass

#Create a task from a function
# kreiranje taska iz funkcije
# skripta ne radi 
def intenzivnaFunkcija():
    # odredjeno izvrsavanje naredbi koje opterecuje procesor
    pass
    
def posao_obavljen():
    # ...koriscenje dobijenih rezultata iz prethodne funkcije
    pass
    
task = QgsTask.fromFunction('intenzivna funkcija', intenzivnaFunkcija, onfinished=posao_obavljen)

# Create a task from a processing algorithm
# kreiranje taska iz algoritama za obradu (procesiranje)
parametri = dict()
kontekst = QgsProcessingContext()
povratna_informacija = QgsProcessingFeedback()

bafer = QgsApplication.instance().processingRegistry().algorithmById('native:buffer')
task = QgsProcessingAlgRunnerTask(bafer, parametri, kontekst, povratna_informacija)

# skripta ne vraca gresku, ali ne vidim njen rezultat




































