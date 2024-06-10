from abc import ABC


class geometric(ABC):

    def volume(self):
        # abstract method
        pass


class Rect(geometric):
    length = 4
    width = 6
    height = 6

    def volume(self):
        return self.length * self.width * self.height


class Sphere(geometric):
    radius = 8

    def volume(self):
        return 1.3 * 3.14 * self.radius * self.radius * self.radius


class Cube(geometric):
    Edge = 5

    def volume(self):
        return self.Edge * self.Edge * self.Edge


class Triangle_3D:
    length = 5
    width = 4

    def volume(self):
        return 0.5 * self.length * self.width


rr = Rect()
ss = Sphere()
cc = Cube()
tt = Triangle_3D()
print("Volume of a rectangle:", rr.volume())
print("Volume of a circle:", ss.volume())
print("Volume of a square:", cc.volume())
print("Volume of a triangle:", tt.volume())