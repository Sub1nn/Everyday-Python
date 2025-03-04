print("This program calculates the average of the 3 numbers you enter. The numbers can be int’s or float’s.")

# for calculating the average dynamically

numbers = []

for i in range(3):
    number = float(input(f"Enter number {i+1}:\n"))
    numbers.append(number)


total_sum = sum(numbers)

average = total_sum / len(numbers)

print(f"Average of the numbers (rounded to 3 decimal places): {round(average, 3)}")
print(f"Average of the numbers (rounded to the closest integer): {round(average)}")
print(f"Average of the numbers as in integer without the decimal part: {int(average)}")
