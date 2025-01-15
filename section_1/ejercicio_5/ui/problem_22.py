from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.problem_22 import Employee

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/problema_22.ui", self)

        # Defining widgwets

        self.employees_name_input = self.findChild(QLineEdit, "employees_name_input")
        self.rate_input = self.findChild(QLineEdit, "rate_input")
        self.worked_hours_input = self.findChild(QLineEdit, "worked_hours_input")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.result_text = self.findChild(QTextEdit, "result_text")

        # Defining actions and controllers

        self.show()
        self.compute_button.clicked.connect(self.compute_result)
        self.clear_button.clicked.connect(self.clear_all)

    def compute_result(self):
        employees_name = self.employees_name_input.text().title()
        rate = float(self.rate_input.text())
        worked_hours = float(self.worked_hours_input.text())

        result_text = Employee(employees_name, rate, worked_hours).compute_salary().print_employees_info()
        self.result_text.setText(result_text)

    def clear_all(self):
        self.employees_name_input.setText('')
        self.rate_input.setText('')
        self.worked_hours_input.setText('')

        self.result_text.setText('')

