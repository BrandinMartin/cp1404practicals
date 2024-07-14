"""
CP1404 Practical 6 - Client code to use the Car class.
"""

from car import Car  # Would not work when I used prac_06.car for some reason


def main():
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
