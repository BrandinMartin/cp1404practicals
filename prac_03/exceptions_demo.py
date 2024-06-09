"""
CP1404 - prac_03
Exceptions Demo
"""

"""Original code"""

# try:
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     fraction = numerator / denominator
#     print(fraction)
# except ValueError:
#     print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# print("Finished.")


"""Questions"""

# 1. When will a ValueError occur?
# Answer: A ValueError will occur when the input isn't an integer.
# 2. When will a ZeroDivisionError occur?
# Answer: ZeroDivisionError will occur when the denominator input is a 0.
# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Yes you could avoid the error by adding a condition to check if the denominator is 0.


"""Updated code to avoid ZeroDivisionError"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
