class SST:

    # class attribute
    prog1 = "Computer Science"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))
        print("I'm studying {}".format(stud1.__class__.prog1))

# Object instantiation
stud1 = SST(input("Enter the name of the first student: "))
stud2 = SST("Enter the name of the second student: ")

# Accessing class methods
stud1.speak()
stud2.speak()
