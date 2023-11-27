from modules import SpeedTest
code = '''
#####################################################################
################# IMPORT OBJECT APPLICATION  ########################
from API.MainWindow import XMainWindow
################# IMPORT PYQT5 QAPPLICATION  ########################
from PyQt5.QtWidgets import QApplication 
#################  IMPORT SYS MODULE   ##############################
import sys
#####################################################################

def main():
  app = QApplication(sys.argv)
  window = XMainWindow()
  window.showMaximized()
  sys.exit()
'''

# if __name__ == "__main__":
#     main()
execute = SpeedTest.calculate_execution_time(code)
print(f"{execute:.3f}")