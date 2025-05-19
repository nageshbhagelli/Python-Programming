#7. Write a Python program that demonstrates the use of try-except-finally blocks.
# For example, attempt to open a file, process its content, and ensure that the file is closed regardless of whether an exception occurs.

def process_file(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        print("File content:", content)
    except FileNotFoundError:
        print("Error: File not found.")
    finally:
        if 'file' in locals():
            file.close()
            print("File closed.")

# Example usage
filename = input("Enter filename: ")
process_file(filename)
