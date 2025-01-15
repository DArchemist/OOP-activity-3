class Employee:
    employees_name: str
    rate: float
    worked_hours: float
    salary: float

    def __init__(self, employees_name: str, rate: float, worked_hours: float):
        self.employees_name = employees_name.title()
        self.rate = rate
        self.worked_hours = worked_hours

    def compute_salary(self) -> object:
        self.salary = self.rate * self.worked_hours
        return self

    def print_employees_info(self) -> str:
        if self.salary > 450000:
            return f'EL EMPLEADO {self.employees_name} DEVENGÓ ${self.salary:.2f}'
        else:
            return f'EL EMPLEADO ES {self.employees_name}'
