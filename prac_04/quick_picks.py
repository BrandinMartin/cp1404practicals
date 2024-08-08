"""
CP1404 - prac_04
"Quick Pick" Lottery ticket generator program
"""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
RANDOM_PICKS = 6


def main():
    quick_picks_amount = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(quick_picks_amount)
    for quick_picks in quick_picks:
        quick_pick_strings = [f"{number:2}" for number in quick_picks]
        print(" ".join(quick_pick_strings))


def generate_quick_picks(quick_picks_amount):
    quick_picks = []
    pick_number = 0
    while pick_number < quick_picks_amount:
        numbers = []
        while len(numbers) < RANDOM_PICKS:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in numbers:
                numbers.append(number)
        numbers.sort()  # Ensures each line of numbers is displayed in sorted (ascending) order.
        quick_picks.append(numbers)
        pick_number += 1
    return quick_picks


main()


# needed to make it so that there was no repeat but i ran out of time unfortunately since i caught it late