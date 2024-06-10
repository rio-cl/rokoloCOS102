from abc import ABC, abstractmethod


class Zinc(ABC):

    def rk(self):
        print("Abstract Base Class")


class Tin():
    def rk(self):
        super().rk()
        print("subclass")


# Object instantiation
r = Tin()
r.rk()
