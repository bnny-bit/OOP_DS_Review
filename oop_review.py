# 1. Encapsulation, Inheritance, and Abstraction (via ABC)
from abc import ABC, abstractmethod

# Abstract Class for Abstraction
class Vehicle(ABC):
    """Abstract base class for all vehicles."""
    def __init__(self, color):
        self._color = color # Protected attribute
    
    @abstractmethod
    def start_engine(self):
        """Abstract method to be overridden by subclasses."""
        pass

    def get_color(self): # Getter method for Encapsulation
        return self._color

# Subclass demonstrating Inheritance and Encapsulation
class Car(Vehicle):
    """A concrete class representing a Car."""
    def __init__(self, color, brand):
        super().__init__(color)
        self.__fuel_level = 100 # Private attribute for Encapsulation
        self.brand = brand

    def start_engine(self): # Overrides the abstract method
        print(f"The {self.brand} engine starts with a roar.")

    def drive(self, distance):
        """A method to simulate driving and check fuel level."""
        # Accessing private variable via a public method (part of Encapsulation)
        if self.__fuel_level > 0:
            self.__fuel_level -= distance // 10
            print(f"Driving {distance} km. Fuel remaining: {self.__fuel_level}%")
        else:
            print("Out of fuel!")

# 2. Polymorphism (Method Overloading is simulated in Python, but Method Overriding is clearer)
class ElectricCar(Car):
    """Subclass to demonstrate Method Overriding (Polymorphism)."""
    def start_engine(self):
        # Overriding the parent's method
        print("The Electric Car silently powers on.")

    # Simulating Method Overloading (though Python uses default arguments)
    def recharge(self, amount=50):
        print(f"Recharging by {amount} units.")


# --- Execution ---
print("--- OOP Demonstration ---")

# Car object
my_car = Car("Red", "Toyota")
print(f"My car is: {my_car.get_color()}")
my_car.start_engine()
my_car.drive(50)

# ElectricCar object (Polymorphism)
my_ev = ElectricCar("Blue", "Tesla")
my_ev.start_engine() # Calls the overridden method
my_ev.recharge(100) # Calls with specific amount
my_ev.recharge()    # Calls with default amount (simulated overloading)
