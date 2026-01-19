import math

def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Eliminate all other even numbers immediately
    if n % 2 == 0:
        return False

    # Check for factors from 3 up to sqrt(n)
    # We skip even numbers in the loop (step=2)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True

# Testing the function
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")