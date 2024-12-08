"""
CP1404 - prac_03
Name file programs
"""

# 1
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.readline().strip()
print(f"Hi {name}!")
in_file.close()

# 3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
result = number1 + number2
print(result)

# 4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
print(total)
