# L05-T4: Compressed string

def compress_string(input_str):
    # Initialize variables
    compressed_str = ""
    count = 1

    # Loop through the string characters, starting from the second character
    for i in range(1, len(input_str)):
        # If the current character is the same as the previous one, increment the count
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            # Add the previous character and its count (if greater than 1) to the compressed string
            compressed_str += input_str[i - 1]
            if count > 1:
                compressed_str += str(count)
            count = 1  # Reset count for the new character

    # Add the last character and its count to the compressed string
    compressed_str += input_str[-1]
    if count > 1:
        compressed_str += str(count)

    return compressed_str

def main():
    # input a string to compress
    original_string = input("Give a string to compress:\n")
    compressed_string = compress_string(original_string)

    # Calculate the compression ratio
    compression_ratio = round(len(compressed_string) / len(original_string), 2)

    print(f"Compressed string: {compressed_string}")
    print(f"Compressing ratio {compression_ratio}")

# Call the main function to run the program
main()

    
