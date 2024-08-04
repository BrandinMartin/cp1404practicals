"""
CP1404 prac_09
Taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            display_choose_taxi(taxis)
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = input("Drive how far? ")
                current_taxi.drive(distance)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def display_choose_taxi(taxis):
    """Display taxi choices"""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    taxi_choice = int(input("Choose taxi: "))
    while taxi_choice < 0 or taxi_choice > 3:
        print("Invalid taxi choice")
        taxi_choice = int(input("Choose taxi"))
    return taxis[taxi_choice]


main()
