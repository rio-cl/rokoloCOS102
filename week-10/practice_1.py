class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name method
    def getname(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here employee method returns true
    def isEmployee(self):
        return True


# Object Instantiation
emp = Person("Segun Da-Silver")  # An Object of Person
print(emp.getname(), emp.isEmployee())

emp = Employee("Omotayo Ayeni")  # An Object of Employee
print(emp.getname(), emp.isEmployee())
