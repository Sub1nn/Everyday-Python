user_int = int(input("Enter a positive integer:\n"))
print(f"Number {user_int} multiplied by itself is {user_int*user_int}")

circle_radius = int(input("Give the radius of a circle as an integer:\n"))

PII = 3.14

area = PII * (circle_radius ** 2)
perimeter = 2 * PII * circle_radius

print(f"The radius of the circle is {circle_radius}, the perimeter is {perimeter} and the area is {area}")

rec_length1 = int(input("Enter the length of one side of the rectangle as an integer:\n"))
rec_length2 = int(input("Enter the length of another side of the rectangle as an integer:\n"))

area_rec = rec_length1 * rec_length2
perimeter_rec = 2 * (rec_length1 + rec_length2)

print(f"The sides of the rectangle are {rec_length1} and {rec_length2}.")
print(f"The perimeter of the rectangle is {perimeter_rec}.")
print(f"The area of the rectangle is {area_rec}.")



