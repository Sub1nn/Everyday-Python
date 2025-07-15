class Person():
    count = 0
    def __init__(self, name, age, city, education):
        self.name = name
        self.age = age
        self.city = city
        self.education = education
        Person.count += 1
    
    def person_details(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Education: {self.education}"
    

Alice = Person("Alice", 30, "New York", "Bachelor's in CS")
Bob = Person("Bob", 25, "Los Angeles", "Master's in Math")
Charlie = Person("Charlie", 28, "Chicago", "PhD in Physics")

print(Alice.person_details())  # Output: Name: Alice, Age: 30, City: New York, Education: Bachelor's in CS
print(Bob.person_details())    # Output: Name: Bob, Age: 25, City: Los Angeles, Education: Master's in Math
print(Charlie.person_details())  # Output: Name: Charlie, Age: 28, City: Chicago, Education: PhD in Physics
print(f"Total number of Person instances created: {Person.count}")  # Output: Total number of Person instances created: 3
# This code defines a Person class with attributes for name, age, city, and education.
# It also includes a method to return the person's details and a class variable to