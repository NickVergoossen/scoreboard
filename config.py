import configparser

from PySide6 import QtWidgets

config = configparser.ConfigParser()
config.read("config.ini")

app = QtWidgets.QApplication()
wid = QtWidgets.QWidget()
wid.setWindowTitle('De titel')
layout = QtWidgets.QFormLayout(wid)
wid.show()

opslaan = QtWidgets.QPushButton('opslaan', wid)
layout.addWidgets(opslaan)
annuleren = QtWidgets.QtPushButton('annuleren', wid)


label = QtWidgets.QLabel("titel:")

button = QtWidgets.QPushButton("verander score", wid)
button.show()
label = QtWidgets.Qlabel("titel font size:")
edit_title_size = QtWidgets.QSpinBox()
edit_title_size.setMaximum(4)
edit_title_size.setMinimum(1000)
edit_title_size.setValue(config["title"].getint("font"))
layout.addRow(label, edit_title_size)

def opgeslagen():
    configfile = open("config.ini", "w")
    config.write(configfile)
    print("opgeslagen")

def geannuleerd():
    print("Geannuleerd")

opslaan.clicked.connect(opgeslagen)
annuleren.clicked.connect(geannuleerd)

app.exec_()

