# It is clearly seen that self and obj is referring to the same object


class Check:
    def __init__(self):
        print("Address of self = ",id(self))


obj = Check()
print("Address of class object = ", id(obj))
