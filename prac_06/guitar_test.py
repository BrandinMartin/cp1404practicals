"""
CP1404 prac_06 - Testing guitar program
Estimated TTC - 50 minutes
Actual TTC - 65 minutes
"""
from guitar import Guitar

CURRENT_YEAR = 2024


def test_guitar():
    """Tests Guitar class functionality"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)  # Couldn't work out how to use differently
    another = Guitar("Another Guitar", 2013, 10000.10)

    print(f"{gibson.name} get_age() - Expected {100}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {9}. Got {another.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected {True}. Got {gibson.is_vintage()}")
    print(f"{another.name} get_age() - Expected {False}. Got {another.is_vintage()}")


if __name__ == '__main__':  # Allows the test to run
    test_guitar()



