from API.UI.ui_newDatabase import  ( Ui_NewDatabase )
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon, QPixmap

class XNewDatabase(QDialog, Ui_NewDatabase):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    
    icon = QIcon()
    icon.addPixmap(QPixmap(":/logos/images.png"), QIcon.Normal, QIcon.Off)
    self.setWindowIcon(icon)

    