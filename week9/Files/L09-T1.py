def input_integer():
    try:
        return int(input("Enter an integer:\n"))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

def main():
    # Prompt for the number of integers to sum
    num_integers = None
    while num_integers is None:
        num_integers = input_integer()
    print(f"Now give {num_integers} integers!")

    # Collect the specified number of integers, handling invalid inputs
    integers = []
    while len(integers) < num_integers:
        number = input_integer()
        if number is not None:
            integers.append(number)
    
    # Calculate and print the sum
    total_sum = sum(integers)
    print(f"The sum of the entered integers is: {total_sum}")

# Run the main function
if __name__ == "__main__":
    main()
