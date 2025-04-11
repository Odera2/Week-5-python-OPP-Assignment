class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        return "Device is now powered on."

class Smartphone(Device):
    def __init__(self, brand, model, storage, color):
        super().__init__(brand, model)
        self.storage = storage
        self.color = color

    def display_info(self):
        return f"Smartphone - Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Color: {self.color}"

# Create an object of the Smartphone class
smartphone = Smartphone("Apple", "iPhone 13", 128, "Blue")
print(smartphone.display_info())
print(smartphone.power_on())
