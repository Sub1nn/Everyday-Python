def is_palindrome(s):
    # Convert the string to lowercase and remove newline character
    cleaned = s.strip().lower()
    # Check if the string is equal to its reverse
    return cleaned == cleaned[::-1]


def main():
    # Ask for the input file name
    input_filename = input("Enter the name of the file to be read:\n")
    output_filename = "Palindromes.txt"
    
    # Open the input and output files explicitly
    input_file = open(input_filename, 'r', encoding='utf-8')
    output_file = open(output_filename, 'w', encoding='utf-8')
    
    try:
        # Process each line in the input file
        for line in input_file:
            # Strip newline and check if it's a palindrome
            row_content = line.strip()
            if len(row_content) == 0:
                continue  # Skip empty lines
            
            # Test for palindrome
            if is_palindrome(row_content):
                print(f"row '{row_content}' is a palindrome.")
                # Write to output file if it is a palindrome
                output_file.write(row_content + '\n')
            else:
                print(f"row '{row_content}' is not a palindrome.")
    
    finally:
        # Close both files
        input_file.close()
        output_file.close()


# Run the main function
main()
