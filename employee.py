import csv
employee_database = "employee_information.csv"


def readFile():
    employee_list = [] #geeksforgeeks(2024)

    with open(employee_database, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_list.append(row)
    return employee_list


entries = readFile()



def display_employees(entries):
    if not entries:
        print("No employee found")
    else:
        for entry in entries:
            print("Name: " + entry["Name"])
            print("Hour Wage: " + str(entry["HourlyWage"]))
            print("Hours Worked: " + str(entry["HoursWorked"]))
            print("-" * 30)

def add_employee(entries):
    id_found = True
    while id_found:
        employee_id = input("Enter employee ID: ")
        id_found = False
        for entry in entries:
            if entry["EmployeeID"] == employee_id:
                print("Employee ID already exists. Please try again.")
                id_found = True

    valid_name = False
    while not valid_name:
        employee_name = input("Enter employee name: ")
        if employee_name.isalpha():
            valid_name = True
        else:
            print("Please use only letters.")

    valid_number = False
    while not valid_number:
        try:
            employee_hourly_wage = float(input("Enter hourly wage: "))
            if employee_hourly_wage < 0:
                print("Please enter a positive number.")
            else:
                valid_number = True
        except ValueError:
            print("Please enter a number.")

    valid_number = False
    while not valid_number:
        try:
            employee_hours_worked = float(input("Enter hours worked: "))
            if employee_hours_worked < 0:
                print("Please enter a positive number.")
            else:
                valid_number = True
        except ValueError:
            print("Please enter a number.")

    entries.append({"EmployeeID": employee_id, "Name": employee_name, "HourlyWage": employee_hourly_wage, "HoursWorked": employee_hours_worked})
    save_employee(entries)
    print("Employee added successfully")


def calculate_salary(entries):
    total_salary = 0
    employee_count = 0
    salaries = []
    found = False
    for entry in entries:
        if "HourlyWage" in entry and "HoursWorked" in entry:
            found = True
            hourly_wage = float(entry["HourlyWage"])
            hours_worked = float(entry["HoursWorked"])
            salary = hourly_wage * hours_worked
            employee_id = entry.get("EmployeeID") #w3schools
            print("Salary of the employee with ID " + str(employee_id) + ": " + str(salary))

            total_salary += salary
            employee_count += 1
            salaries.append(salary)
        else:
            print("No hourly wage or hours worked")

    if not found:
        print("No employee found")

    return total_salary, employee_count, salaries






def search_employee():
    print("Search employee")

def update_hours():
    print("Update hours")

def calculate_average_salary(entries):
    total_salary, employee_count, salaries = calculate_salary(entries)

    if employee_count > 0:
        average_salary = round(total_salary / employee_count)
        min_salary = min(salaries)
        max_salary = max(salaries)
        print("Average salary: " + str(average_salary))
        print("Minimum salary: " + str(min_salary))
        print("Maximum salary: " + str(max_salary))

    else:
        print("No employee found")


def delete_employee():
    employee_id = input("Enter employee ID: ")
    found = False
    for entry in entries:
        if employee_id == entry["EmployeeID"]:

            found = True
            entries.remove(entry)
            print("Employee deleted...")

    if found:
        # Save all changes after the loop completes
        save_employee(entries)

    if not found:
        print("No employee found")

    print("Delete employee")

def save_employee(entries):
    with open(employee_database, 'w') as file:
        headers = ['EmployeeID', 'Name', 'HourlyWage', 'HoursWorked']
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()  #geeksforgeeks(2024)
        writer.writerows(entries) #geeksforgeeks(2024)


while True:
    print("1. View All Employees")
    print("2. Add a New Employee")
    print("3. Calculate Salary")
    print("4. Search for an employee")
    print("5. Update hours worked")
    print("6. Calculate Average/highest/lowest salary among employee")
    print("7. Delete Employee")
    print("8. Save new employee")
    print("9. Exit")

    choice = input("Enter your choice: 1/2/3/4/5/6/7/8/9: ")
    if choice == "1":
        display_employees(entries)
    elif choice == "2":
        add_employee(entries)
    elif choice == "3":
        calculate_salary(entries)
    elif choice == "4":
        search_employee()
    elif choice == "5":
        update_hours()
    elif choice == "6":
        calculate_average_salary(entries)
    elif choice == "7":
        delete_employee()
    elif choice == "8":
        save_employee(entries)
    elif choice == "9":
        print("Exiting....")
        exit()
    else:
        print("Invalid choice")
