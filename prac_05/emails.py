"""
CP1404 - prac_05
emails program
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        name_confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if name_confirmation != "y" and name_confirmation != "":
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    username, domain = email.split('@')
    name_parts = username.split('.')
    name = " ".join(name_parts).title()
    return name


main()
