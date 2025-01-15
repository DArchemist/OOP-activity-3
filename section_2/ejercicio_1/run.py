from PyQt5.QtWidgets import QApplication
import sys
from ui.shapes import UI

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()