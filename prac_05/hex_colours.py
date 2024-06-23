"""
CP1404 prac_05
Hex colour code directory
"""

COLOUR_CODES = {"apricot": "#fbceb1",
                "aqua": "#00ffff",
                "aquamarine1": "#7fffd4",
                "aquamarine2": "#76eec6",
                "asparagus": "#87a96b",
                "aureolin": "#fdee00",
                "azure1": "#f0ffff",
                "azure2": "#e0eeee",
                "beaver": "#9f8170",
                "beige": " #f5f5dc"}


colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()
