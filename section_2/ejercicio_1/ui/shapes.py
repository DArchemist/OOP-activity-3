from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5 import uic
from modules.shapes import Circle, Rectangle, Square, RightRectangle

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("ui/shapes.ui", self)

        # Defining widgwets

        self.radius_input = self.findChild(QLineEdit, "radius_input")

        self.width_input = self.findChild(QLineEdit, "width_input")
        self.height_rectangle_input = self.findChild(QLineEdit, "height_rectangle_input")

        self.side_input = self.findChild(QLineEdit, "side_input")

        self.base_input = self.findChild(QLineEdit, "base_input")
        self.height_triangle_input = self.findChild(QLineEdit, "height_triangle_input")

        self.compute_button_circle = self.findChild(QPushButton, "compute_button_circle")
        self.clear_button_circle = self.findChild(QPushButton, "clear_button_circle")

        self.compute_button_rectangle = self.findChild(QPushButton, "compute_button_rectangle")
        self.clear_button_rectangle = self.findChild(QPushButton, "clear_button_rectangle")

        self.compute_button_square = self.findChild(QPushButton, "compute_button_square")
        self.clear_button_square = self.findChild(QPushButton, "clear_button_square")

        self.compute_button_triangle = self.findChild(QPushButton, "compute_button_triangle")
        self.clear_button_triangle = self.findChild(QPushButton, "clear_button_triangle")


        self.result_text = self.findChild(QTextEdit, "result_text")
        self.result_text_2 = self.findChild(QTextEdit, "result_text_2")
        self.result_text_3 = self.findChild(QTextEdit, "result_text_3")
        self.result_text_4 = self.findChild(QTextEdit, "result_text_4")

        # Defining actions and controllers

        self.show()

        self.compute_button_circle.clicked.connect(self.compute_result_circle)
        self.clear_button_circle.clicked.connect(self.clear_all_circle)

        self.compute_button_rectangle.clicked.connect(self.compute_result_rectangle)
        self.clear_button_rectangle.clicked.connect(self.clear_all_rectangle)

        self.compute_button_square.clicked.connect(self.compute_result_square)
        self.clear_button_square.clicked.connect(self.clear_all_square)

        self.compute_button_triangle.clicked.connect(self.compute_result_triangle)
        self.clear_button_triangle.clicked.connect(self.clear_all_triangle)


    def compute_result_circle(self):
        radius = float(self.radius_input.text())

        circle = Circle(radius)

        result_text = f'El área del círculo es = {circle.get_area()}, El perímetro del círculo es = {circle.get_perimeter()}'
        self.result_text.setText(result_text)

    def clear_all_circle(self):
        self.radius_input.setText('')

        self.result_text.setText('')

    def compute_result_rectangle(self):
        width = float(self.width_input.text())
        height = float(self.height_rectangle_input.text())

        rectangle = Rectangle(width, height)

        result_text = f'El área del rectángulo es = {rectangle.get_area()}, El perímetro del rectángulo es = {rectangle.get_perimeter()}'
        self.result_text_2.setText(result_text)

    def clear_all_rectangle(self):
        self.width_input.setText('')
        self.height_rectangle_input.setText('')

        self.result_text_2.setText('')

    def compute_result_square(self):
        side = float(self.side_input.text())

        square = Square(side)

        result_text = f'El área del cuadrado es = {square.get_area()}, El perímetro del cuadrado es = {square.get_perimeter()}'
        self.result_text_3.setText(result_text)

    def clear_all_square(self):
        self.side_input.setText('')

        self.result_text_3.setText('')

    def compute_result_triangle(self):
        base = float(self.base_input.text())
        height = float(self.height_triangle_input.text())

        rectangle = RightRectangle(base, height)

        result_text = f'El área del triángulo es = {rectangle.get_area()}, El perímetro del triángulo es = {rectangle.get_perimeter()}'
        self.result_text_4.setText(result_text)

    def clear_all_triangle(self):
        self.base_input.setText('')
        self.height_triangle_input.setText('')

        self.result_text_4.setText('')