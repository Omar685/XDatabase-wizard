# self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint)

from PyQt5.QtWidgets import ( 
  QMainWindow, 
  QToolBar,
  QPushButton,
  QAction,
  QMessageBox
)
import pyperclip as pc
from sys import exit

from API.UI.ui_mainwindow import ( Ui_MainWindow )
from API.models.functions import ( 
  new_database_dialog, 
  open_database_dialog
)
from API.models.vars import *
import icons_rc


class XMainWindow(QMainWindow, Ui_MainWindow):
  def __init__(self) -> None:
    super().__init__()
    self.setupUi(self)
    self.setWindowTitle("Database Wizard")
    
    action1 = QAction("Undo", self)
    action2 = QAction("Redo", self)
    action3 = QAction("Quary", self)
    action4 = QAction("Execute", self)

    toolbar = self.addToolBar("Toolbar")
    toolbar.addAction(action1)
    toolbar.addAction(action2)
    toolbar.addAction(action3)
    toolbar.addAction(action4)
    
    self.actionNew_Database.triggered.connect(new_database_dialog)
    self.actionOpen_Database.triggered.connect(open_database_dialog)
    self.actionQuit.triggered.connect(exit)
    self.actionAbout.triggered.connect(self.about)

  def about(self):
    QMessageBox.information(self, "About", INFORMATION)