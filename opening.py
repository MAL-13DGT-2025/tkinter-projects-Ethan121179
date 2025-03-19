import os

def read_file(file_name):
    """Reads the content of a file"""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            print("\nFile content:")
            print(file.read())
    else:
        print(f"The file '{file_name}' does not exist.")

def write_to_file(file_name, content):
    """Writes content to a file"""
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Content has been written to '{file_name}'.")

def search_in_file(file_name, search_term):
    """Searches for a term in the file"""
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            found = False
            for line_number, line in enumerate(lines, start=1):
                if search_term.lower() in line.lower():
                    print(f"Found '{search_term}' on line {line_number}: {line.strip()}")
                    found = True
            if not found:
                print(f"'{search_term}' not found in the file.")
    else:
        print(f"The file '{file_name}' does not exist.")

def menu():
    """Displays the main menu and handles user input"""
    while True:
        print("\n--- File Manager ---")
        print("1. Read a file")
        print("2. Write to a file")
        print("3. Search in a file")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            file_name = input("Enter the file name to read: ")
            read_file(file_name)
        elif choice == '2':
            file_name = input("Enter the file name to write to: ")
            content = input("Enter the content to write: ")
            write_to_file(file_name, content)
        elif choice == '3':
            file_name = input("Enter the file name to search in: ")
            search_term = input("Enter the term to search for: ")
            search_in_file(file_name, search_term)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
