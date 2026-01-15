# Function to handle all the checks
def analyze_number(n):
    # We turn it into a string so we can loop through digits and reverse it easily
    s = str(n)
    num_digits = len(s)
    
    # 1. Even or Odd? (The simplest check)
    parity = "Even" if n % 2 == 0 else "Odd"
    
    # 2. Palindrome? (Check if it's the same backwards)
    is_palindrome = "Yes" if s == s[::-1] else "No"
    
    # 3. Armstrong Number? 
    # (Sum of each digit raised to the power of the total number of digits)
    total = 0
    for digit in s:
        total += int(digit) ** num_digits
    
    is_armstrong = "Yes" if total == n else "No"
    
    # 4. Written Form (Digit by digit)
    words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    written = " ".join(words[int(digit)] for digit in s)

    # Print it out nicely
    print(f"\n--- Results for {n} ---")
    print(f"Even or Odd:  {parity}")
    print(f"Palindrome:   {is_palindrome}")
    print(f"Armstrong:    {is_armstrong}")
    print(f"In Words:     {written}")

# Quick test
num = int(input("Enter a number to test: "))
analyze_number(num)