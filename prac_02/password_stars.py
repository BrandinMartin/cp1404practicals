"""
CP1404 - prac_02
Password Program
"""

MIN_LENGTH = 8


def main():
    """Main function that runs the program"""
    password = get_password()
    validate_password(password)
    print_password_asterisk(password)


def get_password():
    """Asks the user for a password"""
    return input(f"Enter your password: ")


def validate_password(password):
    """Validates the length of the password."""
    while len(password) < MIN_LENGTH:
        print(f"The password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter your password: ")


def print_password_asterisk(password):
    """Prints an asterisk for each character within the password."""
    print('*' * len(password))


main()
