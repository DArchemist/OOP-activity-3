from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.problem_7 import Comparator

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/problema_7.ui", self)

        # Defining widgwets

        self.a_input = self.findChild(QLineEdit, "a_input")
        self.b_input = self.findChild(QLineEdit, "b_input")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.result_text = self.findChild(QTextEdit, "result_text")

        # Defining actions and controllers

        self.show()
        self.compute_button.clicked.connect(self.compute_result)
        self.clear_button.clicked.connect(self.clear_all)

    def compute_result(self):
        a = float(self.a_input.text())
        b = float(self.b_input.text())
        result_text = Comparator.compare(a, b)
        self.result_text.setText(result_text)

    def clear_all(self):
        self.a_input.setText('')
        self.b_input.setText('')

        self.result_text.setText('')

