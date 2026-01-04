
try:
    print("Reading file content:\n")

    file = open("sample.txt", 'rt')

    """
    file.write("This is a sample text.\n")
    file.write("Have a  nice day!")
    """

    line1=file.readline()
    line2=file.readline()

    print(f"Line 1: {line1}")
    print(f"Line 2: {line2}")

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")