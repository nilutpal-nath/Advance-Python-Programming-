# File Handling and I/O Reading/Writing
# Experiment 8: Based on the file handling operations and pseudocode

def process_file_data(input_filename, output_filename):
    # Step 1: Write sample data into input file for demonstration purposes
    with open(input_filename, "w") as infile:
        infile.write("Line 1: This is the first line.\n")
        infile.write("Line 2: This is the second line.\n")
        infile.write("Line 3: This is the third line.\n")
        infile.write("Line 4: This is the fourth line.\n")

    # Step 2: Open the input file in read mode
    with open(input_filename, "r") as infile:
        # Read all lines from the file into a list
        lines = infile.readlines()

    # Step 3: Count the number of lines
    total_lines = len(lines)
    print(f"Total number of lines: {total_lines}")

    # Step 4: Extract the first two lines
    extracted_lines = lines[:2]

    # Step 5: Open the output file in write mode and write extracted lines
    with open(output_filename, "w") as outfile:
        outfile.writelines(extracted_lines)

    print(f"Extracted lines successfully written to {output_filename}")


# Main Program
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    
    process_file_data(input_file, output_file)
    
    # Verify output file content
    print("\nContent of output.txt:")
    with open(output_file, "r") as f:
        print(f.read())