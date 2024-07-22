# Expanation of this code

# Functions
# make_file(filename):
# Purpose: Creates a new file with the specified name.
# Implementation:
# Tries to create a new file using the open function with mode "x" (exclusive creation mode).
# If the file is created successfully, it prints a success message.
# If a file with the same name already exists, it prints an error message.
# If any other error occurs, it prints a generic error message.
# check_list():
# Purpose: Lists all files in the current directory.
# Implementation:
# Uses os.listdir() to get a list of all files and directories in the current directory.
# If no files are present, it prints a message indicating so.
# Otherwise, it prints the names of all files in the directory.
# write_file(filename):
# Purpose: Writes user input to a specified file.
# Implementation:
# Checks if the specified filename is a file using os.path.isfile().
# If it is a file, it opens the file in write mode and writes user input to it.
# If the file does not exist, it prints an error message.
# Handles FileNotFoundError and other exceptions, printing appropriate error messages.
# read_file(filename):
# Purpose: Reads and prints the content of a specified file.
# Implementation:
# Tries to open the file in read mode.
# Reads the file content and prints it.
# Handles FileNotFoundError and other exceptions, printing appropriate error messages.
# delete_file(filename):
# Purpose: Deletes a specified file.
# Implementation:
# Tries to remove the file using os.remove().
# Handles FileNotFoundError and other exceptions, printing appropriate error messages.
# Update_file(filename):
# Purpose: Updates the content of a specified file.
# Implementation:
# Tries to open the file in write mode.
# Writes user input to the file.
# Handles FileNotFoundError and other exceptions, printing appropriate error messages.
# Main Program
# main():
# Purpose: Provides a menu-driven interface for the file management system.
# Implementation:
# Continuously displays a menu with options to create, write, read, update, list, and delete files, or exit the program.
# Based on the user’s choice, it calls the appropriate function.
# If the user chooses to exit, it prints a closing message, waits for 3 seconds, and then terminates the program.
# If the user inputs an invalid option, it prints an error message and prompts the user to select a valid option.
# Execution
# The main() function is called at the end of the script to start the program.
# The user interacts with the program through the menu.
# Depending on the user's input, the corresponding function is executed.



import os
import time
import os.path
def make_file(filename):
    try:
        with open(filename , "x") as f:
            print(f"Your file with name {filename} is created succesfully")
    except FileExistsError:
        print("File with this name is already exit")
    except Exception as e:
        print("Error has been occured")
   
def check_list():
    files = os.listdir()
    if not files:
        print("No files is present")
    else:
        print("The files preset is ....")
        for file in files:
            print(file)
def write_file(filename):
    try:
        if os.path.isfile(filename):
          print("Yes. it is a file")
          with open(filename , "w") as f:
            content = input("Enter the Content = ")
            filename = f.write(content)
            print("You successfuly write in this file")
        else:
            print(f"The file with this {filename} is not present")
    except FileNotFoundError:
        print("Your file is not exit")
    except Exception as e:
        print("An error is occured")

def read_file(filename):
    try:
        with open(filename,"r") as f:
            content = f.read()
            print(f"Your '{filename}' : \n{content}")
    except FileNotFoundError:
        print("Your file is not exit")
    except Exception as e:
        print("An error is occured")
def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("Your file is not exit")
    except Exception as e:
        print("An error is occured")
def Update_file(filename):
    try:
        with open(filename, "w") as f:
            content = input("Enter the content you want to add = ")
            f.write(content + "\n")
            print(f"Content added to {filename} successfully")
    except FileNotFoundError:
        print("Your file is not exit")
    except Exception as e:
        print("An error is occured")
def main():
    while True:
        print("/////////////////////////File Management System///////////////////////////")
        print("1.Create File")
        print("2.Write File")
        print("3.Read File")
        print("4.Update File")
        print("5.View all File")
        print("6.Remove File")
        print("7.Exit")
        choice = int(input("Enter the choice in the Above given = "))
        if choice == 1 :
            filename = input("Enter the Name of Textfile = ")
            make_file(filename)
        elif choice == 2 :
            filename = input("Enter the the filename in which you want to write = ")
            write_file(filename)
        elif choice == 3 :
            filename = input("Enter the name of file you want to read = ")
            read_file(filename)
        elif choice == 4 :
            filename = input("Enter the filename you want to update = ")
            Update_file(filename)
        elif choice == 5 :
            check_list()
        elif choice == 6 :
            filename = input("Enter the filename you want to Delete = ")
            delete_file(filename)
        elif choice == 7 :
            print("Thanks for using this Program")
            print("Closing.....")
            time.sleep(3)
            print("This Program is close succesfully")
            break
        else:
            print("Invalid Input")
            print("Please Select the Above Option")
# if __name__ == "__main___":
#     main()
main()

        
