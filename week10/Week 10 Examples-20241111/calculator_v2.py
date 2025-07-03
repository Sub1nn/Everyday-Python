# This is a module called calculator.py

# Define a constant
PI = 3.14159

# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract two numbers
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Test the functions if this script is run directly
if __name__ == "__main__":
    print("Testing calculator functions:")
    print("Addition of 5 and 3:", add(5, 3))
    print("Subtraction of 5 and 3:", subtract(5, 3))
    print("Multiplication of 5 and 3:", multiply(5, 3))
    print("Division of 5 by 3:", divide(5, 3))
    print("Division of 5 by 0:", divide(5, 0))
