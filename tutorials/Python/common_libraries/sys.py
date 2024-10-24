import sys

# Accessing command-line arguments
print("Command-line arguments:", sys.argv)

# Exiting the program with a specific exit code
def exit_program():
    print("Exiting the program with exit code 1")
    sys.exit(1)

# Checking the Python interpreter version
if sys.version_info[0] < 3:
    print("Please use Python 3.")
    exit_program()

# Adding a directory to Python's search path for modules
sys.path.append('/path/to/custom/module/directory')

# Iterating over standard input (stdin)
print("Enter text (type 'exit' to stop):")
for line in sys.stdin:
    if 'exit' in line:
        break
    print("You entered:", line.strip())

# Writing to standard output (stdout) and standard error (stderr)
sys.stdout.write("This is a standard output message.\n")
sys.stderr.write("This is a standard error message.\n")

# Getting the platform (operating system)
print("Platform:", sys.platform)
