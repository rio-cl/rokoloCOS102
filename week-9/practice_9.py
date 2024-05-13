class Program:

    # default constructor
    def __init__(self):
        self.course = "CSC 102 - Introduction to Problem Solving"

    # a method for printing data members
    def print_course(self):
        print(self.course)


# creating object of the class
obj = Program()

# calling the instance method using the object obj
obj.print_course()