# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/NewDatabase.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewDatabase(object):
    def setupUi(self, NewDatabase):
        NewDatabase.setObjectName("NewDatabase")
        NewDatabase.resize(527, 230)
        NewDatabase.setMinimumSize(QtCore.QSize(527, 230))
        NewDatabase.setMaximumSize(QtCore.QSize(527, 230))
        self.titleLabel = QtWidgets.QLabel(NewDatabase)
        self.titleLabel.setGeometry(QtCore.QRect(191, 10, 145, 24))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setMouseTracking(False)
        self.titleLabel.setObjectName("titleLabel")
        self.input_name = QtWidgets.QLineEdit(NewDatabase)
        self.input_name.setGeometry(QtCore.QRect(100, 89, 151, 20))
        self.input_name.setPlaceholderText("")
        self.input_name.setObjectName("input_name")
        self.defaulte_rafio = QtWidgets.QRadioButton(NewDatabase)
        self.defaulte_rafio.setGeometry(QtCore.QRect(8, 124, 71, 20))
        self.defaulte_rafio.setObjectName("defaulte_rafio")
        self.input_path = QtWidgets.QLineEdit(NewDatabase)
        self.input_path.setGeometry(QtCore.QRect(84, 150, 321, 20))
        self.input_path.setObjectName("input_path")
        self.line = QtWidgets.QFrame(NewDatabase)
        self.line.setGeometry(QtCore.QRect(0, 40, 527, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.enLabel = QtWidgets.QLabel(NewDatabase)
        self.enLabel.setGeometry(QtCore.QRect(7, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.enLabel.setFont(font)
        self.enLabel.setObjectName("enLabel")
        self.epLabel = QtWidgets.QLabel(NewDatabase)
        self.epLabel.setGeometry(QtCore.QRect(8, 151, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.epLabel.setFont(font)
        self.epLabel.setObjectName("epLabel")
        self.toolButton = QtWidgets.QToolButton(NewDatabase)
        self.toolButton.setGeometry(QtCore.QRect(412, 149, 31, 21))
        self.toolButton.setObjectName("toolButton")
        self.connectBtn = QtWidgets.QPushButton(NewDatabase)
        self.connectBtn.setGeometry(QtCore.QRect(440, 200, 75, 23))
        self.connectBtn.setObjectName("connectBtn")

        self.retranslateUi(NewDatabase)
        QtCore.QMetaObject.connectSlotsByName(NewDatabase)

    def retranslateUi(self, NewDatabase):
        _translate = QtCore.QCoreApplication.translate
        NewDatabase.setWindowTitle(_translate("NewDatabase", "New Database"))
        self.titleLabel.setText(_translate("NewDatabase", "New Database"))
        self.input_name.setText(_translate("NewDatabase", "mydb.db"))
        self.defaulte_rafio.setText(_translate("NewDatabase", "Defualt"))
        self.input_path.setText(_translate("NewDatabase", "E:\\My Projects\\database-wizard\\2023DATABASE"))
        self.enLabel.setText(_translate("NewDatabase", "Enter Name:"))
        self.epLabel.setText(_translate("NewDatabase", "Enter Path:"))
        self.toolButton.setText(_translate("NewDatabase", "..."))
        self.connectBtn.setText(_translate("NewDatabase", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewDatabase = QtWidgets.QDialog()
    ui = Ui_NewDatabase()
    ui.setupUi(NewDatabase)
    NewDatabase.show()
    sys.exit(app.exec_())
