#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

# Extract command-line arguments (excluding the script name)
arguments = sys.argv[1:]

# Convert arguments to integers and calculate the sum
result = sum(map(int, arguments))

# Print the result followed by a new line
print(result)
