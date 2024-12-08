"""
CP1404 prac_06 - Languages program
Estimated time to complete:  30 minutes
Actual time to complete: 35 minutes (71 minutes combined)
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]  # List that contains the three existing ProgrammingLanguage objects

    print("The dynamically typed languages are: ")  # loop through and print names of all languages with dynamic typing
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
