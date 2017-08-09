""" qtmain.py

Contains the PyQt code that sets up the FTSpecViewer UI.

"""

from PyQt5.QtWidgets import QApplication, QWidget

class ftviewerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'FTSpecViewer'
        self.left = 10
        self.top = 10
        self.width = 1280
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
