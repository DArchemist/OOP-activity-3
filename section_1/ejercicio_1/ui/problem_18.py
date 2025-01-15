from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.problem_18 import Employee

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/problema_18.ui", self)

        # Defining widgwets

        self.employees_code_input = self.findChild(QLineEdit, "employees_code_input")
        self.employees_name_input = self.findChild(QLineEdit, "employees_name_input")
        self.worked_hours_input = self.findChild(QLineEdit, "worked_hours_input")
        self.rate_input = self.findChild(QLineEdit, "rate_input")
        self.tax_percentage_input = self.findChild(QLineEdit, "tax_percentage_input")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.result_text = self.findChild(QTextEdit, "result_text")

        # Defining actions and controllers

        self.show()
        self.compute_button.clicked.connect(self.compute_result)
        self.clear_button.clicked.connect(self.clear_all)

    def compute_result(self):
        employees_code = int(self.employees_code_input.text())
        employees_name = self.employees_name_input.text().title()
        worked_hours = float(self.worked_hours_input.text())
        rate = float(self.rate_input.text())
        tax_percentage = float(self.tax_percentage_input.text())

        result_text = Employee(employees_code, employees_name, worked_hours, rate, tax_percentage).compute_salary_info().print_employees_info()
        self.result_text.setText(result_text)

    def clear_all(self):
        self.employees_code_input.setText('')
        self.employees_name_input.setText('')
        self.worked_hours_input.setText('')
        self.rate_input.setText('')
        self.tax_percentage_input.setText('')

        self.result_text.setText('')

