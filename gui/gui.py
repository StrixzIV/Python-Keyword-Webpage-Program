import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import uic #This was a causing so much trouble, but I figured it out eventually.
#from python.foxnews import *

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.searchButton = None
        self.ui = None
        self.loadUI()
        self.searchButton.clicked.connect(lambda: self.printValue())


    def loadUI(self):
        self.ui = uic.loadUi("app.ui", self)
        self.show()


    def printValue(self):
        print(self.searchEdit.text())





def runProgram():
    app = QApplication(sys.argv)

    window = GUI()
    window.show()

    try:
        sys.exit(app.exec_())

    except SystemExit:
        print("Program Closed")



runProgram()
