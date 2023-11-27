import subprocess
from API.newDatabase import XNewDatabase
from API.openDatabase import XOpenDatabase
from PyQt5.QtWidgets import QMessageBox


def execute(file: str, setWhere=None):
  result = subprocess.run(["python", file], capture_output=True, text=True)

  if result.stderr:
      print("Error: ")
      print(result.stderr)
  else:
    print("stdout: ")
    print(result.stdout)

def new_database_dialog():
  app = XNewDatabase()
  app.exec()

def open_database_dialog():
  app = XOpenDatabase()
  app.exec()

