from main import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

def run_FTSpecViewer():
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run_FTSpecViewer()
