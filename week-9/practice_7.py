# A class with init method

class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Hans Madugu')
p.say_hi()
