from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.problem_19 import EquilateralTriangle

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/problema_19.ui", self)

        # Defining widgwets

        self.side_input = self.findChild(QLineEdit, "side_input")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.result_text = self.findChild(QTextEdit, "result_text")

        # Defining actions and controllers

        self.show()
        self.compute_button.clicked.connect(self.compute_result)
        self.clear_button.clicked.connect(self.clear_all)

    def compute_result(self):
        side = float(self.side_input.text())
        triangle = EquilateralTriangle(side)
        result_text = f'EL PERÍMETRO, LA ALTURA, Y EL ÁREA DEL TRIÁNGULO EQUILÁTERO CON LADO {triangle.side:.2f} SON {triangle.get_perimeter():.2f}, {triangle.get_height():.2f}, Y {triangle.get_area():.2f}, RESPECTIVAMENTE.'
        self.result_text.setText(result_text)

    def clear_all(self):
        self.side_input.setText('')

        self.result_text.setText('')

