# Python program to demonstrate error if we
# forget to invoke __init__() of the parent.

class A:
    def __init__(self, n='Emmanuel Abbah'):
        self.name = n




class B(A):
    def __init__(self, roll):
        self.roll = roll

        A.__init__(self, n='Emmanuel Abbah')


# Object Instance
object = B(23)
print(object.name)
