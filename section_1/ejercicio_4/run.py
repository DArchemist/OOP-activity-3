from PyQt5.QtWidgets import QApplication
import sys
from ui.problem_10 import UI

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()