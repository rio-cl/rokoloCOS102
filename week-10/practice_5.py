# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother:
    motherName = "Caroline Aina"

    def mother(self):
        print(self.motherName)


# Base class2
class Father:
    fathername = "Paul Abiodun"

    def father(self):
        print(self.fathername)


# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.motherName)


# Object Instance
s1 = Son()
s1.parents()
