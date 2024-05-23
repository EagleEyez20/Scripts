
# This is how to read an external file. Always remember to close the file.
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()


