"""
CP1404 - prac_02
Program to determine score status
"""

import random


def main():
    """Main function that asks the user for their score and prints the result then it gets a random score/result."""
    score = float(input("Enter your score: "))
    result = determine_status(score)
    print(result)
    random_score = random.randint(0, 100)
    result = determine_status(random_score)
    print(f"\nRandom score: {random_score}")
    print(result)


def determine_status(score):
    """Determines the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
