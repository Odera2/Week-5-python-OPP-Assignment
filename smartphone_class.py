class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Color: {self.color}"

    def make_call(self, number):
        return f"Calling {number}..."

# Create an object of the Smartphone class
phone = Smartphone("Apple", "iPhone 13", 128, "Blue")
print(phone.display_info())
print(phone.make_call("123-456-7890"))
