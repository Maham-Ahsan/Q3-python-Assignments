class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employees):
        self.employees = employees

employee = Employee("Maham")
department = Department([employee])

print(department.employees[0].name)