# Python program to demonstrate
# single inheritance


# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")


# Object Instance
obj = Child()
obj.func1()
obj.func2()
