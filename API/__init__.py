#####################################################################
################# IMPORT OBJECT APPLICATION  ########################
from API.MainWindow import XMainWindow
################# IMPORT PYQT5 QAPPLICATION  ########################
from PyQt5.QtWidgets import QApplication, QWidget
#################  IMPORT SYS MODULE   ##############################
import sys
#####################################################################


def main():
  app = QApplication(sys.argv)
  window = XMainWindow()
  window.showMaximized()
  sys.exit(app.exec_())