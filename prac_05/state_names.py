"""
CP1404 - prac_05
State names in a dictionary program
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}


for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")  # Unsure if I should define a max len for 'code' or if '3' is ok since output matches.

state_code = input("Enter short state: ").upper()

while state_code != "":
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
