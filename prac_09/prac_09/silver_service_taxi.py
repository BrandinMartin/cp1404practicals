"""
CP1404 prac_09
Silver Service Taxi
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Version of a Taxi that includes fanciness (a float that multiplies the price_per_km)"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance based on the parent class Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness  # If the class variable for all taxis goes up the price chance is inherited

    def get_fare(self):
        """Calculate the fare using Taxi function and adding flagfall"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall included"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
