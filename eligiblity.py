# Get age input from the user and convert it to an integer
age = int(input("Enter your age: "))

# Check if the user is 18 or older
if age >= 18:
    print("You are eligible to vote!")
else:
    # Calculate how many years they have left to wait
    years_left = 18 - age
    print(f"You are not eligible. Please wait {years_left} more year(s).")
