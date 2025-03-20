# Leap Year Checker

year = int(input("Enter a year:\n"))  # User input for the year

# Leap year logic
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")  
else:
    print(f"{year} is not a leap year.")
