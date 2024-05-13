class Dogs:

    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name


# Object instantiation
dog1 = Dogs("Oscar")
dog2 = Dogs("Peaches")

# Accessing class attributes
print("Oscar is a {}".format(dog1.__class__.attr1))
print("Peaches is also a {}".format(dog2.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(dog1.name))
print("My name is {}".format(dog2.name))