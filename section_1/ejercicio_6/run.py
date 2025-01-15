from PyQt5.QtWidgets import QApplication
import sys
from ui.problem_23 import UI

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()