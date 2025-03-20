# L03-T3: Simple Calculator with Menu
# Performing basic operations on two integers.

# Getting user inputs for two numbers
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

# Displaying options to the user
print("The calculator can perform the following operations:")
print("1) Add\n2) Subtract\n3) Multiply\n4) Divide")


print(f"The numbers you entered are {num1} and {num2}")
operation = int(input("Select the operation (1-4):\n"))

# Performing the selected operation
if operation == 1:
    print(f"Selection 1: {num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"Selection 2: {num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"Selection 3: {num1} * {num2} = {num1 * num2}")
elif operation == 4:
    if num2 == 0:
        print("Error: Zero cannot be used as a divisor.")
    else:
        result = round(num1 / num2, 2)
        print(f"Selection 4: {num1} / {num2} = {result}")
else:
    print("The operation was not recognized.")  # Invalid operation
