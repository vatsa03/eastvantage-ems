from entities.employee import Employee
from services.company import Company

def print_menu():
    print("\nPlease Enter Your Choice:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. List Employees in Department")
    print("4. Add Department")
    print("5. Remove Department")
    print("6. List Departments")
    print("7. Save Company Data")
    print("8. Load Company Data")
    print("9. Exit")


def main():
    company = Company()
    print("\nWelcome to Employee Management System:")
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department = input("Enter department: ")
            if department in company.departments:
                employee = Employee(name, emp_id, title, department)
                company.departments[department].add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{department}' does not exist.")

        elif choice == '2':
            department = input("Enter department: ")
            if department in company.departments:
                employee_name = input("Enter employee name: ")
                employees = company.departments[department].employees
                for emp in employees:
                    if emp.name == employee_name:
                        company.departments[department].remove_employee(emp)
                        break
                else:
                    print(f"Employee {employee_name} not found in {department}.")
            else:
                print(f"Department '{department}' does not exist.")

        elif choice == '3':
            department = input("Enter department: ")
            if department in company.departments:
                company.departments[department].list_employees()
            else:
                print(f"Department '{department}' does not exist.")

        elif choice == '4':
            department_name = input("Enter department name: ")
            company.add_department(department_name)

        elif choice == '5':
            department_name = input("Enter department name: ")
            company.remove_department(department_name)

        elif choice == '6':
            company.display_departments()

        elif choice == '7':
            filename = input("Enter filename to save company data: ")
            company.save_company_data(filename)
            print("Company data saved.")

        elif choice == '8':
            filename = input("Enter filename to load company data: ")
            company.load_company_data(filename)
            print("Company data loaded.")

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
