"""
CP1404 prac_07
"""

from guitar import Guitar
import csv

FILENAME = 'guitars.csv'


def main():
    guitars = read_guitars(FILENAME)



def read_guitars(filename):
    """Read all the guitars and store them in a list of Guitar objects"""
    guitars = []
    with open(filename, 'r') as infile:
        for line in infile:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2].strip())
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


if __name__ == "__main__"
    main()