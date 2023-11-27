from API.UI.ui_openDatabase import  ( Ui_OpenDatabase )
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QPixmap

class XOpenDatabase(QDialog, Ui_OpenDatabase):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    
    icon = QIcon()
    icon.addPixmap(QPixmap(":/logos/images.png"), QIcon.Normal, QIcon.Off)
    self.setWindowIcon(icon)

    