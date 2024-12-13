import math

# Function to calculate the square root of a number
def calculate_square_root(num):
    return math.sqrt(num)

# Function to calculate the square of a number
def calculate_square(num):
    return num ** 2

# Function to calculate the cube of a number
def calculate_cube(num):
    return num ** 3

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Function to calculate the factorial of a number
def calculate_factorial(num):
    if num < 0:
        return "Undefined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num + 1):
            factorial *= i
        return factorial

# Function to find the prime factors of a number
def prime_factors(num):
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

# Main program
number = int(input("Enter a number: "))

print(f"Square root of {number} is {calculate_square_root(number):.2f}")
print(f"Square of {number} is {calculate_square(number)}")
print(f"Cube of {number} is {calculate_cube(number)}")
print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")
print(f"Factorial of {number} is {calculate_factorial(number)}")
print(f"Prime factors of {number} are {prime_factors(number)}")

