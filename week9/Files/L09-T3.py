import math

def valueError():
    """Handles ValueError by trying to take the square root of a non-negative integer."""
    try:
        number = int(input("Give a non-negative integer: \n"))
        if number < 0:
            raise ValueError("Non-negative number expected for square root.")
        result = math.sqrt(number)
        print(f"Square root of {number} is {result:.2f}.")
    except ValueError:
        print("ValueError happened. Non-negative number expected for square root.")

def indexError():
    """Handles IndexError by accessing an index in a list that may not exist."""
    sample_list = [11, 22, 33, 44, 55]
    try:
        index = int(input("Input index 0-4: \n"))
        print(f"List value is {sample_list[index]} at index {index}.")
    except IndexError:
        print(f"Got an IndexError with index {index}.")
    except ValueError:
        print("ValueError happened. Enter the index as an integer.")

def zeroDivisionError():
    """Handles ZeroDivisionError by dividing 4 by a given number."""
    try:
        divider = int(input("Enter divider: \n"))
        result = 4 / divider
        print(f"4/{divider} = {result:.2f}.")
    except ZeroDivisionError:
        print(f"ZeroDivisionError occurred, divider {divider}.")
    except ValueError:
        print("ValueError happened. Enter the divider as a number.")

def typeError():
    """Handles TypeError by trying to multiply two strings."""
    try:
        number = input("Enter number:\n")
        result = number * number  # This line is intentionally wrong to trigger TypeError
        print(f"Result: {result}")
    except TypeError:
        print("Got TypeError. Two strings cannot be multiplied together.")

def main():
    while True:
        print("What do you want to do:")
        print("1) Test for ValueError")
        print("2) Test for IndexError")
        print("3) Test for ZeroDivisionError")
        print("4) Test for TypeError")
        print("0) Stop")
        
        try:
            choice = int(input("Your choice:\n"))
        except ValueError:
            print("ValueError happened. Enter the selection as an integer.")
            while True:
                try:
                    choice = int(input("Your choice:\n"))
                    break
                except ValueError:
                    print("ValueError happened. Enter the selection as an integer.")
        
        if choice == 0:
            print("See you again!")
            break
        elif choice == 1:
            valueError()
        elif choice == 2:
            indexError()
        elif choice == 3:
            zeroDivisionError()
        elif choice == 4:
            typeError()
        else:
            print("Unknown selection, please try again.")

# Run the program
if __name__ == "__main__":
    main()
