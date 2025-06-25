import math
import random

def calculate_area_of_circle():
    radius = int(input("Enter the radius of the circle as an integer:\n"))
    area = math.pi * math.pow(radius, 2)
    print(f"With a radius of {radius}, the area of the circle is {area:.2f}.\n")

def guess_random_number():
    random.seed(1)  # Set seed for reproducibility
    target = random.randint(0, 1000)
    attempts = 0
    
    print("Guess the integer drawn by the program.")
    while True:
        guess = int(input("Enter an integer between 0 and 1000:\n"))
        attempts += 1
        
        if guess < target:
            print("The requested number is higher.")
        elif guess > target:
            print("The requested number is lower.")
        else:
            print(f"Correct! You used {attempts} tries to guess the correct integer.\n")
            break

def main():
    print("This program uses libraries to solve tasks.")
    
    while True:
        print("What do you want to do:\n1) Calculate the area of the circle\n2) Guess the number\n0) Stop")
        choice = input("Your choice:\n")
        
        if choice == '1':
            calculate_area_of_circle()
        elif choice == '2':
            guess_random_number()
        elif choice == '0':
            print("See you again!")
            break
        else:
            print("Unknown choice, please try again.\n")

if __name__ == "__main__":
    main()
