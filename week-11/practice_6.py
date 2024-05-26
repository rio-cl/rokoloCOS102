# base class
class Company:
    # base constructor
    def __init__(self):
        # Protected instance variable
        self._project = "Blockchain Development"


# child class
class Employee(Company):
    # child constructor
    def __init__(self, name):
        self.name = name

        # invoke base constructor
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)

        # Accessing protected instance variable in child class
        print("Working on project :", self._project)


c = Employee("Prince Ibekwe")
c.show()

# Direct access to protected instance variable
print('Project:', c._project)