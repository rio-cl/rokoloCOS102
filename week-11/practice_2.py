class Employee:

    # constructor
    def __init__(self, name, salary):
        # public instance variables
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public instance variables
        print("Name: ", self.name, 'Salary:', "N%s" % (self.salary))


# creating object of a class
emp = Employee('Abdurrahman', 500000)

# accessing public instance variables
print("Name: ", emp.name, 'Salary:', "N{}".format(emp.salary))

# calling public method of the class
emp.show()