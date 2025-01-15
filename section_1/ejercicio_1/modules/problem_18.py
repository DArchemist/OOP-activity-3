class Employee:
    # First we define the variables
    employees_code: int
    employees_name: str
    worked_hours: float
    rate: float
    tax_percentage: float
    gross_salary: float
    tax: float
    net_salary: float

    # Then we define a constructor method to create a new Employee object
    
    def __init__(self, employees_code: int, employees_name: str, worked_hours: float, rate: float, tax_percentage: float):
        self.employees_code = employees_code
        self.employees_name = employees_name.title()
        self.worked_hours = worked_hours
        self.rate = rate
        self.tax_percentage = tax_percentage

    # Now a method to compute the salary info

    def compute_salary_info(self) -> object:
        self.__compute_gross_salary()
        self.__compute_tax()
        self.__compute_net_salary()
        return self
    
    # Now we define private methods to compute the gross salary, the taxes, and the net salary
    
    def __compute_gross_salary(self) -> None:
        self.gross_salary = self.worked_hours * self.rate

    def __compute_tax(self) -> None:
        self.tax = self.gross_salary * self.tax_percentage / 100

    def __compute_net_salary(self) -> None:
        self.net_salary = self.gross_salary - self.tax

    # Finally, we define a function for printing the employee info

    def print_employees_info(self) -> None:
        return f"EL CÓDIGO DEL EMPLEADO ES: {self.employees_code}, EL NOMBRE DEL EMPLEADO ES: {self.employees_name}, EL SALARIO BRUTO ES: ${self.gross_salary:.2f}, EL SALARIO NETO ES: ${self.net_salary:.2f}"