from fractions import Fraction

# Function to get a fraction from user input
def get_fraction():
    numerator = int(input("Give numerator (top):\n"))
    denominator = int(input("Give denominator (bottom):\n"))
    return Fraction(numerator, denominator)

# Main function
def main():
    print("Give the first fraction.")
    fraction1 = get_fraction()
    
    print("Give the second fraction.")
    fraction2 = get_fraction()
    
    exponent = int(input("Give an exponent:\n"))
    
    # Performing operations
    sum_result = fraction1 + fraction2
    subtract_result = fraction1 - fraction2
    multiply_result = fraction1 * fraction2
    divide_result = fraction1 / fraction2
    power_result = fraction1 ** exponent
    
    # Displaying results
    print(f"Sum: {fraction1} + {fraction2} = {sum_result}")
    print(f"Subtract: {fraction1} - {fraction2} = {subtract_result}")
    print(f"Multiply: ({fraction1}) * ({fraction2}) = {multiply_result}")
    print(f"Divide: ({fraction1}) / ({fraction2}) = {divide_result}")
    print(f"Power: ({fraction1})**{exponent} = {power_result}")

# Run the program
main()
