"""
CP1404 - prac_02
Score menu program
"""

MENU = """(G)et a valid score
(P)rint result 
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            print(f"Score: {score}")
        elif choice == 'P':
            score = int(input("Enter score: "))
            print(print_result(score))
        elif choice == 'S':
            score = int(input("Enter score: "))
            print(show_stars(score))
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()


def get_valid_score():
    score = int(input("Enter a valid score (0-100 inclusive): "))
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        return score


def print_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    return '*' * score


main()
