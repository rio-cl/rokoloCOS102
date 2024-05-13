# Another example using SELF

class Car:

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


toyota = Car("Toyota Corolla", "blue")
kia = Car("Kia Cerato", "green")

toyota.show()
# same output as car.show(toyota)

kia.show()
# same output as car.show(kia)
