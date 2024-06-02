"""
CP1404 - prac_02
Password Program
"""

MIN_LENGTH = 8

password = input("Enter your password: ")

while len(password) < MIN_LENGTH:
    print(f"Password must be at least {MIN_LENGTH} characters long.")
    password = input("Enter your password: ")

print('*' * len(password))
