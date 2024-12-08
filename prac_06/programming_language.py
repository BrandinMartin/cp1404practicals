"""
CP1404 prac_06 - Programming languages program
Estimated time to complete:  30 minutes
Actual time to complete: 35 minutes (71 minutes combined)
"""


class ProgrammingLanguage:
    """Establishes a simple class for a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Create fields for the programming languages and set them to the parameters passed in"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed by returning True/False"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string detailing the ProgrammingLanguage statement"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
