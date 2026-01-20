class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Employee:
    def __init__(self, emp_id, name, role):
        self.emp_id = emp_id
        self.name = name
        self.role = role

class BusinessManager:
    def __init__(self, business_name):
        self.name = business_name
        self.inventory = {}
        self.employees = []
        self.total_sales = 0.0

    def add_product(self, name, price, stock):
        self.inventory[name] = Product(name, price, stock)
        print(f"Added {name} to inventory.")

    def add_employee(self, emp_id, name, role):
        new_emp = Employee(emp_id, name, role)
        self.employees.append(new_emp)
        print(f"Registered employee: {name}")

    def process_sale(self, product_name, quantity):
        if product_name in self.inventory and self.inventory[product_name].stock >= quantity:
            cost = self.inventory[product_name].price * quantity
            self.inventory[product_name].stock -= quantity
            self.total_sales += cost
            print(f"Sale successful! Total: ${cost:.2f}")
        else:
            print("Error: Out of stock or product not found.")

    def show_report(self):
        print(f"\n--- {self.name} Business Report ---")
        print(f"Total Revenue: ${self.total_sales:.2f}")
        print(f"Inventory Levels: {[(p.name, p.stock) for p in self.inventory.values()]}")
        print(f"Staff Count: {len(self.employees)}")

# --- Execution ---
my_biz = BusinessManager("TechNova Solutions")
my_biz.add_product("Laptop", 1200, 10)
my_biz.add_employee(101, "Alice Smith", "Manager")
my_biz.process_sale("Laptop", 2)
my_biz.show_report()