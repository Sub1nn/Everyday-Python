def read_value(file):
    try:
        line = file.readline()
        if not line:
            print("End of values, end the program.")
            return 0
        return int(line.strip())

    except ValueError:
        print("Error reading value.")
        return 0


def main():
    inputFileName = input("Enter the name of the file to read:\n")

    inputFile = open(inputFileName, 'r')
    outputFile = open("Exercise5_output.txt", 'w')
    
    try:
        while True:
            print("This calculator can perform the following functions:\n1) Enter the values\n2) Sum\n3) Subtract\n4) Multiply\n5) Divide\n0) Stop")

            choice = int(input("Select the function (0-5):\n"))

            if choice == 1:
                a = read_value(inputFile)
                
                   
                b = read_value(inputFile)
                
                    
                print(f"Values {a} and {b} were read")

            elif choice in [2, 3, 4, 5]:
                if a is None or b is None:
                    print("End of values, end the program.")
                    
                
                elif choice == 2:
                    result = a + b
                    outputFile.write(f"sum {a} + {b} = {result}\n")
                    print("Result saved in file.")

                elif choice == 3:
                    result = a - b
                    outputFile.write(f"subtract {a} - {b} = {result}\n")
                    print("Result saved in file.")

                elif choice == 4:
                    result = a * b
                    outputFile.write(f"multiply {a} * {b} = {result}\n")
                    print("Result saved in file.")

                elif choice == 5:
                    if b == 0:
                        outputFile.write("Cannot divide by zero.\n")
                        print("Result saved in file.")
                    
                    else:
                        result = a / b
                        outputFile.write(f"division {a} / {b} = {result}\n")
                        print("Result saved in file.")


            elif choice == 0:
                print("Stopping")
                break
            
            else:
                print("Invalid selection. Please try again.")

    except ValueError:
        print("Error: Please check your selection")

    
    inputFile.close()
    outputFile.close()


main()
