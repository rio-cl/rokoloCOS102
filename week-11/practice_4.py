class Employee:

    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name

        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, '\nSalary:', self.__salary)


# creating object of a class
emp = Employee('Chikaodi Chinaka', 250000)

# calling public method of the class
emp.show()