print("This program calculates the average of the 3 numbers you enter.")
print("The numbers can be int's or float's.")

num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
num3 = float(input("Enter the third number:\n"))

# sum of the numbers
total_sum = num1 + num2 + num3
print(f"Sum of the numbers: {total_sum}")

# average of the numbers
average = total_sum / 3

print(f"Average of the numbers (rounded to 3 decimal places): {round(average, 3)}")
# print(f"{average:.3f}") => fixed point notation, number formatted as decimal number
print(f"Average of the numbers (rounded to the closest integer): {round(average)}")
print(f"Average of the numbers as an integer without the decimal part: {int(average)}")
