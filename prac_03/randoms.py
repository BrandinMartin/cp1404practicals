"""
CP1404 - prac_03
Random numbers
"""

import random

"""Questions"""

# print(random.randint(5, 20))  # line 1
# Question 1a: What did you see on line 1?
# Answer: I saw '11' on line 1.
# Question 1b: What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number I could have seen is 5 and the largest is 20.

# print(random.randrange(3, 10, 2))  # line 2
# Question 2a: What did you see on line 2?
# Answer: I saw '3' on line 2.
# Question 2b: What is the smallest number you could have seen, what was the largest?
# Answer: The smallest number I could have seen is 3 and the largest is 9.

# print(random.uniform(2.5, 5.5))  # line 3
# Question 3a: What did you see on line 3?
# Answer: I saw '5.442511941146367' on line 3.
# Question 3b: What is the smallest number you could have seen, what was the largest?
# Answer: The smallest number I could have seen is 2.5 and the largest number is 5.5.

"""Produces a random number between 1 and 100 inclusive"""
print(random.randint(1, 100))
