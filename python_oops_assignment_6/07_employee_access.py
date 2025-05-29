class Employee:
    def __init__(self, name, _salary, __ssn):
        self.name = name
        self._salary = _salary
        self.__ssn = __ssn

    def display(self):
        print(f"Name: {self.name} Salary: {self._salary} Ssn: {self.__ssn}")

# Creating object
emp = Employee("Maham", 95000, "9000555")

print("Accessing variables from outside the class:")
print(f"Public name: {emp.name}")         # ✅ Allowed
print(f"Protected salary: {emp._salary}") # ⚠️ Technically allowed, but discouraged
# print(f"Private SSN: {emp.__ssn}")      # ❌ Error! Cannot access directly

# Accessing private variable 
print("emp._Employee__ssn: ", emp._Employee__ssn) # ✅ Works, but not best practice
