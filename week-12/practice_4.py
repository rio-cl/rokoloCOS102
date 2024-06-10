from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def move(self):
        pass


class Human(Animals):

    def move(self):
        print("I can walk and run")


class Snake(Animals):

    def move(self):
        print("I can crawl")


class Dog(Animals):

    def move(self):
        print("I can bark")


class Lion(Animals):

    def move(self):
        print("I can roar")


# Object Instantiation
R = Human()
R.move()

K = Snake()
K.move()

r = Dog()
r.move()

k = Lion()
k.move()
