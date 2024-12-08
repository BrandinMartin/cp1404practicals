"""
CP1404 prac_09
UnreliableCar test
"""
from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class functionality"""
    my_unreliable_car = UnreliableCar("Unreliable", 100, 10)
    my_reliable_car = UnreliableCar("Reliable", 100, 100)

    for i in range(1, 11):
        print(f"Test {i} ({i}km)")
        print(f"{my_unreliable_car.name:10} drove {my_unreliable_car.drive(i):2}km")
        print(f"{my_reliable_car.name:10} drove {my_reliable_car.drive(i):2}km\n")

    print("Summary:")
    print(my_unreliable_car)
    print(my_reliable_car)


main()
