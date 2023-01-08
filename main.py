class Vehicle:
    def __int__(self, name, speed,  mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

        def seating_capacity(self, capacity):
            return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)



School_bus = Bus("Volvo", 180, 12)
print(School_bus.seating_capacity())


