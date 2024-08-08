"""
CP1404 prac_09
Unreliable Car program
"""
from random import uniform
from car import Car


class UnreliableCar(Car):
    """Version of a Car that includes reliability (a float between 0-100 representing % chance of successful drive)"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on the parent Class Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random_number < reliability"""
        random_number = uniform(0, 100)  # return a random float between 0 and 100
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0

        return distance_driven  # return distance driven even if it is 0km
