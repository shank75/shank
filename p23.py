# NOTE_ : Before running the program create a "student.info.txt" file in the same folder as this program.

# Function to add student information to the file
def add_student_info(file_name, roll_number, name, division, address):
    with open(file_name, 'a') as file:
        file.write(f"{roll_number},{name},{division},{address}\n")

# Function to delete student information from the file
def delete_student_info(file_name, roll_number):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    with open(file_name, 'w') as file:
        for line in lines:
            if line.split(',')[0] != roll_number:
                file.write(line)

# Function to display information of a particular student
def display_student_info(file_name, roll_number):
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split(',')
            if data[0] == roll_number:
                print("Roll Number:", data[0])
                print("Name:", data[1])
                print("Division:", data[2])
                print("Address:", data[3])
                return
    print("Student record not found.")

# Main function
def main():
    file_name = "student_info.txt"
    while True:
        print("\n1. Add Student Information")
        print("2. Delete Student Information")
        print("3. Display Student Information")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            division = input("Enter Division: ")
            address = input("Enter Address: ")
            add_student_info(file_name, roll_number, name, division, address)
            print("Student information added successfully.")

        elif choice == '2':
            roll_number = input("Enter Roll Number to delete: ")
            delete_student_info(file_name, roll_number)
            print("Student information deleted successfully.")

        elif choice == '3':
            roll_number = input("Enter Roll Number to display: ")
            display_student_info(file_name, roll_number)

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
