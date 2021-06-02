import configparser

from PySide6 import QtWidgets

config = configparser.ConfigParser()
config.read("config.ini")

app = QtWidgets.QApplication()
wid = QtWidgets.QWidget()
wid.setWindowTitle('De titel')
wid.show()

layout = QtWidgets.QFormLayout(wid)

label = QtWidgets.QLabel("titel:")

button = QtWidgets.QPushButton("verander score", wid)
button.show()
label = QtWidgets.Qlabel("titel font size:")
edit_title_size = QtWidgets.QSpinBox()
edit_title_size.setMaximum(4)
edit_title_size.setMinimum(1000)
edit_title_size.setValue(config["title"].getint("font"))
layout.addRow(label, edit_title_size)

def select_team_a_logo():
    result = QtWidgets.QFileDialog.getOpenFileName()
    filename = result[0]
    button_team_a_logo.setText(filename)
    print(filename)
    return filename

app.exec_()

