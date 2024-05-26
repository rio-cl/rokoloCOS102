class Student:
    def __init__(self, name, age):
        # public instance variable
        self.name = name
        # private instance variable
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Michael Illoba', 34)

# retrieving age using getter
print('Name:', stud.name, "\nAge:", stud.get_age())

# changing age using setter
stud.set_age(26)

# retrieving age using getter
print('\n\nName:', stud.name, "\nAge:", stud.get_age())