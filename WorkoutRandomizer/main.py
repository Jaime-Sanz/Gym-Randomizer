import pandas
import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
from sklearn.utils import shuffle

dfAbs = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                          sheet_name='Abs')
dfBack = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                           sheet_name='Back')
dfBiceps = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                             sheet_name='Biceps')
dfCalves = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                             sheet_name='Calves')
dfCardio = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                             sheet_name='Cardio')
dfChest = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                            sheet_name='Chest')
dfLegs = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                           sheet_name='Legs')
dfShoulders = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                                sheet_name='Shoulders')
dfTriceps = pandas.read_excel('/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/workoutRandomizer.xlsx',
                              sheet_name='Triceps')


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Load The UI File
        uic.loadUi("/Users/jaimesanchez/Desktop/PythonScripts/WorkoutRandomizer/mygui.ui", self)

        # Define Widgets
        self.groupNumber = self.findChild(QSpinBox, "groupNumber")
        self.generateWorkout = self.findChild(QPushButton, "pushButton")
        self.abs = self.findChild(QCheckBox, "absCheck")
        self.back = self.findChild(QCheckBox, "backCheck")
        self.biceps = self.findChild(QCheckBox, "bicepsCheck")
        self.calves = self.findChild(QCheckBox, "calvesCheck")
        self.cardio = self.findChild(QCheckBox, "cardioCheck")
        self.chest = self.findChild(QCheckBox, "chestCheck")
        self.legs = self.findChild(QCheckBox, "legsCheck")
        self.shoulders = self.findChild(QCheckBox, "shouldersCheck")
        self.triceps = self.findChild(QCheckBox, "tricepsCheck")

        # Show The App
        self.show()

        # Widgets Process
        self.generateWorkout.clicked.connect(self.data)

    def data(self):
        if self.abs.isChecked():
            sAbs = shuffle(dfAbs)
            print(sAbs.head(self.groupNumber.value()))
        if self.back.isChecked():
            sBack = shuffle(dfBack)
            print(sBack.head(self.groupNumber.value()))
        if self.biceps.isChecked():
            sBiceps = shuffle(dfBiceps)
            print(sBiceps.head(self.groupNumber.value()))
        if self.calves.isChecked():
            sCalves = shuffle(dfCalves)
            print(sCalves.head(self.groupNumber.value()))
        if self.cardio.isChecked():
            sCardio = shuffle(dfCardio)
            print(sCardio.head(self.groupNumber.value()))
        if self.chest.isChecked():
            sChest = shuffle(dfChest)
            print(sChest.head(self.groupNumber.value()))
        if self.legs.isChecked():
            sLegs = shuffle(dfLegs)
            print(sLegs.head(self.groupNumber.value()))
        if self.shoulders.isChecked():
            sShoulders = shuffle(dfShoulders)
            print(sShoulders.head(self.groupNumber.value()))
        if self.triceps.isChecked():
            sTriceps = shuffle(dfTriceps)
            print(sTriceps.head(self.groupNumber.value()))


# Initializing The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()
