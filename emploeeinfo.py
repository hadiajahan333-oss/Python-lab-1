employees = []

for i in range(3):
    print("Enter information for Employee", i + 1)

    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))

    employee = (name, age, salary)
    employees.append(employee)

print("\nAll Employees:")
print(employees)