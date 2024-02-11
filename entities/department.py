class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"Employee {employee.name} removed from {self.name}")
        else:
            print(f"Employee {employee.name} not found in {self.name}")

    def list_employees(self):
        print(f"Employees in department {self.name}:")
        for employee in self.employees:
            print(employee)