"""
CP1404 prac_07 - Guitar program
"""
CURRENT_YEAR = 2024
VINTAGE_THRESHOLD = 50


class Guitar:
    """Guitar class for storing one guitar with their respective attributes"""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar with name, year, cost attributes"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Uses string formatting to return something matching the sample values"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Decides if the guitar is vintage or not by returning True/False depending on the age"""
        return self.get_age() >= VINTAGE_THRESHOLD

    def __lt__(self, other):
        """Compares Guitar and other by year"""
        return self.year < other.year
