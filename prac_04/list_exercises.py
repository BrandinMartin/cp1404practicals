"""
CP1404 - prac_04
List Exercises
"""

"""Basic list operations program"""

numbers = []

for i in range(5):
    number = float(input(f"Number: "))
    numbers.append(number)

print(f"The first number is {numbers[0]:.0f}")  # Added :.0f to ensure output aligns with sample output
print(f"The last number is {numbers[-1]:.0f}")
print(f"The smallest number is {min(numbers):.0f}")  # Was unsure if I should use variables then print
print(f"The largest number is {max(numbers):.0f}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")


"""Woefully inadequate security checker program"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
