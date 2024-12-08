"""
CP1404 - prac_03
String formatting program
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16036

print(f"{year} {name} for about ${cost:,}!")

for i in range(11):
    print(f"2 ^{i:2} is {2 ** i:4}")
