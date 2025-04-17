import os

def process_file(input_filename, output_filename):
    """
    Reads a file, modifies its contents, and writes the modified content to a new file.
    Handles potential errors such as file not found and read/write errors.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        # Attempt to open the input file in read mode ('r')
        with open(input_filename, 'r') as infile:
            # Read the entire content of the input file
            content = infile.read()
            # Print a success message to the console
            print(f"Successfully read from {input_filename}")

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Attempt to open the output file in write mode ('w')
        with open(output_filename, 'w') as outfile:
            # Write the modified content to the output file
            outfile.write(modified_content)
            # Print a success message to the console
            print(f"Successfully wrote to {output_filename}")

    # Handle the case where the input file does not exist
    except FileNotFoundError:
        print(f"Error: File not found - {input_filename}")
        # Optionally, you could create the file if it doesn't exist:
        # with open(input_filename, 'w') as f:
        #     f.write("")  # Create an empty file
        #     print(f"Created empty file: {input_filename}")

    # Handle errors that may occur during reading or writing the file
    except IOError as e:
        print(f"Error: An I/O error occurred - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to run the file processing program.
    Prompts the user for the input filename and calls the process_file function.
    """
    # Prompt the user to enter the name of the input file
    input_filename = input("Enter the name of the input file: ")
    # Define the name of the output file
    output_filename = "output.txt"  # Hardcoded output filename

    # Call the process_file function to perform the file operations
    process_file(input_filename, output_filename)

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()

