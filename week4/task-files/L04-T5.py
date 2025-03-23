# L04-T5: Menu-based program

# while true creats an infinite loop to keep the program running for continuous interaction
while True:
    print("This calculator can perform the following functions:")
    print("1) Enter numbers")
    print("2) Sum")
    print("3) Subtract")
    print("4) Multiplication")
    print("5) Division")
    print("6) Power of")
    print("0) Stop")
    
    choice = int(input("Select function (0-6):\n"))

    if choice == 0:
        print("Stopping")
        print("Bye")
        break  # Exit the loop when user selects '0'

    elif choice == 1:
        num1 = int(input("Enter the first number:\n"))
        num2 = int(input("Enter the second number:\n"))
        print(f"You entered numbers {num1} and {num2}")

    elif choice == 2:
        print(f"Sum {num1} + {num2} = {num1 + num2}")

    elif choice == 3:
        print(f"Subtraction {num1} - {num2} = {num1 - num2}")

    elif choice == 4:
        print(f"Multiplication {num1} * {num2} = {num1 * num2}")

    elif choice == 5:
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print(f"Division {num1} / {num2} = {round(num1 / num2, 2)}")

    elif choice == 6:
        print(f"Power of {num1}**{num2} = {num1 ** num2}")

    else:
        print("Unknown selection, try again.")
