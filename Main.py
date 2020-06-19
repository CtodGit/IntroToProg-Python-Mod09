# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# CTod,6.17.2020, Used for module assignment
# CTod,6.17.2020, Used for module, added import section, added variables used
# CTod,6.17.2020, Got function for each menu option, issues with print current list
# CTod,6.18.2020, Fixed print current list issues, commented code, completed assignment (LATE)
# ------------------------------------------------------------------------ #

# imports modules needed for program
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # employee class child of person
    import ProcessingClasses as P   # processing classes
    from IOClasses import EmployeeIO as Eio  # Employee input class
    print('This file is the starting point of my program!')  # A note to make sure it's running main
else:
    raise Exception("This file was not created to be imported")

# Data -------------------------------------------------------------------- #
file_name = "C:\\_PythonClass\\Assignment09\\EmployeeData.txt"
list_of_rows = []
lstFileData = []
lstTable = []
first_name = ''
last_name = ''

#see DataClasses.py for Person and Employee objects (for storing data to objects)
# ------------------------------------------------------------------------ #

# Processing ------------------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
lstEmpData = P.FileProcessor.read_data_from_file(file_name)
lstTable.clear()

# list loop, creats emp object, populates it with employee properties from file
for list in lstEmpData:
    emp = Emp(list[0], list[1], list[2].strip())
    lstTable.append(emp)

# ------------------------------------------------------------------------ #

# Main Body of Script  ---------------------------------------------------- #

# Loop for main
while True:
    # Show user a menu of options
    Eio.print_menu_items()

    # Get user's menu option choice
    user_input = Eio.input_menu_options()

    # Show user current data in the list of employee objects
    if user_input == '1':
        Eio.print_current_list_items(lstTable)
    # Let user add data to the list of employee objects
    elif user_input== '2':
        emp = Eio.input_employee_data()
        lstTable.append(emp)
    # let user save current data to file
    elif user_input == '3':
        P.FileProcessor.save_data_to_file(file_name, lstTable)
    # Let user exit program
    elif user_input == '4':
        print('Have a nice day... or night. Exiting now...')
        exit()

# Main Body of Script: END  ---------------------------------------------------- #
