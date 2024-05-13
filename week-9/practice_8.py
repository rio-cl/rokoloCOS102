# Another class with init method
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Method
    def say_hi(self):
        print('Hello, my name is', self.name)

# Creating different objects


p1 = Person('Enobasi')
p2 = Person('Leela')
p3 = Person('Divine')

p1.say_hi()
p2.say_hi()
p3.say_hi()
