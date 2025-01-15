from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.problem_10 import Student

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/problema_10.ui", self)

        # Defining widgwets

        self.enrollment_number_input = self.findChild(QLineEdit, "enrollment_number_input")
        self.students_name_input = self.findChild(QLineEdit, "students_name_input")
        self.patrimony_input = self.findChild(QLineEdit, "patrimony_input")
        self.estrato_social_input = self.findChild(QLineEdit, "estrato_social_input")

        self.compute_button = self.findChild(QPushButton, "compute_button")
        self.clear_button = self.findChild(QPushButton, "clear_button")

        self.result_text = self.findChild(QTextEdit, "result_text")

        # Defining actions and controllers

        self.show()
        self.compute_button.clicked.connect(self.compute_result)
        self.clear_button.clicked.connect(self.clear_all)

    def compute_result(self):
        enrollment_number = int(self.enrollment_number_input.text())
        students_name = str(self.students_name_input.text()).title()
        patrimony = float(self.patrimony_input.text())
        estrato_social = int(self.estrato_social_input.text())

        result_text = Student(enrollment_number, students_name, patrimony, estrato_social).compute_tuition().print_students_info()
        self.result_text.setText(result_text)

    def clear_all(self):
        self.enrollment_number_input.setText('')
        self.students_name_input.setText('')
        self.patrimony_input.setText('')
        self.estrato_social_input.setText('')

        self.result_text.setText('')

