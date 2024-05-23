
# This code is to read a file and print it to the screen

#employee_file = open("anyfile.txt", "r")
#print(employee_file.read())
#employee_file.close()


# This is to appened to a file. Must use the \n to add a new line in the file.
#employee_file = open("anyfile.txt", "a")
#employee_file.write("Toby - Human Resources")
#employee_file.close()


# This is to write to a file. The below will overwrite all the contents of the file and replace with the new line below.
#employee_file = open("anyfile.txt", "w")
#employee_file.write("Kelly - Customer Service")
#employee_file.close()

# This will create a new file if it does not exist with this one entry.
employee_file = open("anyfile1.txt", "w")
employee_file.write("Kelly - Customer Service")
employee_file.close()

