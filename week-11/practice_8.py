class Student:
    # Contructor
    def __init__(self, name, roll_no, age):
        # public instance variable
        self.name = name
        # private instance variables to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    def get_roll_no(self):
        return self.__roll_no

    # setter method to modify instance varaible
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number


# object instanc=tiation
info = Student('David Usim', 10, 15)

# before Modify
info.show()

# changing roll number using setter
info.set_roll_no(120)


info.set_roll_no(25)
info.show()
