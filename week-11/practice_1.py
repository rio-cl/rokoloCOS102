# A program that displays employees information

class Employee:

    # constructor
    def __init__(self, name, salary, project):
        # instance variables
        self.name = name
        self.salary = salary
        self.project = project

    # method to display employee's details
    def show(self):
        # accessing public instance variables
        print("\nName: ", self.name, '\nSalary:', "N" + str(self.salary))

    # method
    def work(self):
        print(self.name, 'is working on', self.project)


name = input("Enter your name: ")
salary = int(input("How much do you earn: "))
project = input("What project are you working on: ")

# creating object of a class
emp = Employee(name, salary, project)

# calling public method of the class
emp.show()
emp.work()
