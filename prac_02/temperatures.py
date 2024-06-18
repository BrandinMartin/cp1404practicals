"""
CP1404 - prac_02
Revised temperature conversion program
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    make_choice()


def make_choice():
    user_choice = input(">>> ").upper()
    while user_choice != "Q":
        if user_choice == "C":
            celsius = float(input("Enter temperature (Celsius): "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif user_choice == "F":
            fahrenheit = float(input("Enter temperature (Fahrenheit): "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        user_choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
