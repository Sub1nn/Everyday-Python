# L03-T4: Grade Calculation Based on Points
# Assigning grades based on points.

# User input for points
points = float(input("Enter your number of points:\n"))  

# Assigning grades based on the points range
if 90 <= points <= 100:
    grade = 5
elif 80 <= points < 90:
    grade = 4
elif 70 <= points < 80:
    grade = 3
elif 60 <= points < 70:
    grade = 2
elif 50 <= points < 60:
    grade = 1
else:
    grade = 0

print(f"Your grade is: {grade}")
