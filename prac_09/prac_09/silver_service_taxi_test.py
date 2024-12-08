"""
CP1404 prac_09
Silver Service Taxi test
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class functionality"""

    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(fancy_taxi.get_fare())


if __name__ == '__main__':
    main()
