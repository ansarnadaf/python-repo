def check_attendance():
    # List of students in the class
    students = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
    attendance = {}

    print("--- Class Attendance System ---")
    print("Enter 'p' for Present and 'a' for Absent.\n")

    for student in students:
        while True:
            status = input(f"Is {student} present? (p/a): ").lower()
            if status == 'p':
                attendance[student] = "Present"
                break
            elif status == 'a':
                attendance[student] = "Absent"
                break
            else:
                print("Invalid input. Please enter 'p' or 'a'.")

    # Displaying the final report
    print("\n--- Attendance Summary ---")
    print(f"{'Student Name':<15} | {'Status'}")
    print("-" * 30)
    
    present_count = 0
    for name, status in attendance.items():
        print(f"{name:<15} | {status}")
        if status == "Present":
            present_count += 1

    # Show statistics
    total = len(students)
    print("-" * 30)
    print(f"Total Students: {total}")
    print(f"Present: {present_count}")
    print(f"Absent: {total - present_count}")

if __name__ == "__main__":
    check_attendance()