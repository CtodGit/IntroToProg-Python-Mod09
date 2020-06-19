# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CTod,6.17.2020 modified to check through lab modules
# CTod. 6.17.2020 modified to check assignment modules
# ---------------------------------------------------------- #


if __name__ == "__main__":
    from DataClasses import Employee as Emp # employee class child of person
    import ProcessingClasses as P   # processing classes
    from IOClasses import EmployeeIO as Eio # Employee input class
    print('This file is the starting point of my program!')
else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# # Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for list in lstFileData:
    lstTable.append(Emp(list[0], list[1], list[2].strip()))
for row in lstTable:
    print(row.to_string().strip(), type(row))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
