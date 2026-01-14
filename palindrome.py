def is_palindrome(num):
    # Convert number to string and compare with its reverse [::-1]
    return str(num) == str(num)[::-1]

# Testing the function
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")