class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def display_info(self):
        task_list = ", ".join(self.tasks) if self.tasks else "No tasks assigned"
        print(f"ID: {self.emp_id} | Name: {self.name} | Position: {self.position} | Tasks: {task_list}")

class Office:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, position, salary):
        new_emp = Employee(emp_id, name, position, salary)
        self.employees[emp_id] = new_emp
        print(f"Employee {name} added successfully.")

    def assign_task(self, emp_id, task):
        if emp_id in self.employees:
            self.employees[emp_id].add_task(task)
            print(f"Task '{task}' assigned to {self.employees[emp_id].name}.")
        else:
            print("Employee not found.")

    def show_all_employees(self):
        print("\n--- Office Staff Directory ---")
        for emp in self.employees.values():
            emp.display_info()

# --- Execution ---
my_office = Office()

# Adding Staff
my_office.add_employee(101, "Alice Smith", "Manager", 75000)
my_office.add_employee(102, "Bob Jones", "Developer", 60000)

# Assigning Work
my_office.assign_task(101, "Review Q1 Reports")
my_office.assign_task(102, "Fix Login Bug")

# Displaying Report
my_office.show_all_employees()