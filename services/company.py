import json
from entities.department import Department
from entities.employee import Employee

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department_name):
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department {department_name} added.")
        else:
            print(f"Department {department_name} already exists.")

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department {department_name} removed.")
        else:
            print(f"Department {department_name} not found.")

    def display_departments(self):
        print("Departments:")
        for department_name in self.departments:
            print(department_name)

    def save_company_data(self, filename):
        with open(filename, 'w') as file:
            data = {'departments': {}}
            for dept_name, dept_obj in self.departments.items():
                data['departments'][dept_name] = [emp.__dict__ for emp in dept_obj.employees]
            json.dump(data, file, indent=4)

    def load_company_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            for dept_name, employees in data['departments'].items():
                new_department = Department(dept_name)
                for emp in employees:
                    new_employee = Employee(emp['name'], emp['emp_id'], emp['title'], emp['department'])
                    new_department.add_employee(new_employee)
                self.departments[dept_name] = new_department