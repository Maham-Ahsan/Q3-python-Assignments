class Car:

    def __init__(self, brand):
        self.brand = brand
        
    def start(self):
        print(f"{self.brand} is starting")

my_Car = Car("Suzuki")
print(my_Car.brand)
my_Car.start()