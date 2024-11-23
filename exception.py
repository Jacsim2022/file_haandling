def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ")
        
        # Try to open the input file
        with open(input_file, 'r') as file:
            content = file.readlines()

        # Modify the content (e.g., convert to uppercase for demonstration)
        modified_content = [line.upper() for line in content]

        # Ask for the output filename
        output_file = input("Enter the name of the file to write: ")
        
        # Write the modified content to the output file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Content successfully written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading/writing a file: {e}")

# Run the function
read_and_write_file()
