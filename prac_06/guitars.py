"""
CP1404 prac_06 - Playing the Guitars
Estimated TTC - 60 minutes
Actual TTC -  minutes
"""

from guitar import Guitar


def main():
    """Program managing the guitars within the Guitar class"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    print("These are my guitars: ")


main()
