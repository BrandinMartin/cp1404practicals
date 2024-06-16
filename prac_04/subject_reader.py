"""
CP1404 - prac_04
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print_subject_details(data)


def load_data():
    """Loads data from a text file and returns it as a nested list"""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        data.append(parts)
    input_file.close()
    return data


def print_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
