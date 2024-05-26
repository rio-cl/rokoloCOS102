class Employee:
    # constructor
    def __init__(self, name, salary):
        # public instance variable
        self.name = name

        # private variable
        self.salary = salary


# creating object of a class
emp = Employee('Oyindamola Apampa', 900000)

# direct access to public instance variable
print('Name:', emp.name)

# direct access to private instance variable using name mangling
print('Salary:', "N" + str(emp.salary))