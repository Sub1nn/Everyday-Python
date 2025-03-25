# L05-T5: Menu-based program / Calculator. 

def menu():
    print("Select one of the following operations:")
    print("1) Enter integers")
    print("2) Sum")
    print("3) Subtract")
    print("4) Multiplication")
    print("5) Division")
    print("0) Stop")
    choice = int(input("Select the function (0-5):\n"))  
    return choice

def enter_integer(text):
    return int(input(text))

def sum(value1, value2):
    result = value1 + value2
    return f"Sum {value1} + {value2} = {result}"

def subtract(value1, value2):
    result = value1 - value2
    return f"Subtract {value1} - {value2} = {result}"

def multiplication(value1, value2):
    result = value1 * value2
    return f"Multiplication {value1} * {value2} = {result}"

def division(value1, value2):
    if value2 == 0:
        return "You cannot divide by zero."
    else:
        result = round(value1 / value2, 2)
        return f"Division {value1} / {value2} = {result}"

def main():
    value1 = None
    value2 = None

    while True:
        choice = menu()
        
        if choice == 1:
            value1 = enter_integer("Enter first integer: \n")  
            value2 = enter_integer("Enter second integer: \n")  
            print(f"You inputted integers {value1} and {value2}")
        
        elif choice == 2:
            if value1 is not None and value2 is not None:
                print(sum(value1, value2))
            else:
                print("Please enter integers first.")
        
        elif choice == 3:
            if value1 is not None and value2 is not None:
                print(subtract(value1, value2))
            else:
                print("Please enter integers first.")
        
        elif choice == 4:
            if value1 is not None and value2 is not None:
                print(multiplication(value1, value2))
            else:
                print("Please enter integers first.")
        
        elif choice == 5:
            if value1 is not None and value2 is not None:
                print(division(value1, value2))
            else:
                print("Please enter integers first.")
        
        elif choice == 0:
            print("Bye.")
            break
        
        else:
            print("Unknown choice, try again.")

# Call the main function to start the program
main()
