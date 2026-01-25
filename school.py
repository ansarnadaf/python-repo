class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def display_info(self):
        return f"ID: {self.id_number} | Name: {self.name} | Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, id_number, grade):
        super().__init__(name, age, id_number)
        self.grade = grade

    def display_info(self):
        base_info = super().display_info()
        return f"[Student] {base_info} | Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, age, id_number, subject):
        super().__init__(name, age, id_number)
        self.subject = subject

    def display_info(self):
        base_info = super().display_info()
        return f"[Teacher] {base_info} | Subject: {self.subject}"

class SchoolManagement:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"Teacher {teacher.name} added successfully.")

    def show_all(self):
        print(f"\n--- {self.school_name} Records ---")
        for t in self.teachers:
            print(t.display_info())
        for s in self.students:
            print(s.display_info())

# --- Implementation Example ---
my_school = SchoolManagement("Greenwood Academy")

# Adding data
s1 = Student("Alice Smith", 15, "S101", "10th")
t1 = Teacher("Mr. Harrison", 45, "T505", "Physics")

my_school.add_student(s1)
my_school.add_teacher(t1)

# Displaying everything
my_school.show_all()