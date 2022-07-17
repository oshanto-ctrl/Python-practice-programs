__author__ = "Rejoan"

import string
import sys
from random import randint, choice

def generate_random_password(mn, mx):
    """
    Generates a random password consist of ascii_leters
    and digits.
    """ 
    value = string.ascii_letters + string.digits + string.punctuation
    random_password = "".join(choice(value) for ch in range(randint(mn, mx)))
    print(f"\n\tpassword = {random_password}\n\tpassword-length = {len(random_password)}\n")

def check_parameter_of_password(mn, mx):
    """
    Reviews user given parameters before generating password.
    """
    # is int or not -> print error massege and exit program
    if not isinstance(mn, int) and isinstance(mx, int):
        prompt = f"Checker: invalid maximum minimum parameter for password! Try again."
        sys.exit(prompt)
    # is mn > mx -> print error message
    elif mn > mx:
        prompt = f"Checker: invalid input parameter for password! Try again."
        sys.exit(prompt)
    else:
        generate_random_password(mn, mx)

# Driver
welcome_prompt = f"\n\tWelcome User.\n\tTo generate your password first fill-up 2 parameters.\n\t(Tips: Use at least 12 characters as minimum for your password)\n"
print(welcome_prompt)
try:
    min_char = int(input("\tMinimum Character for your password: "))
    max_char = int(input("\tMaximum Character for your password: "))
except ValueError:
    print(f"Wrong parameter entered for maximum or minimum length for password!")
else:
    check_parameter_of_password(min_char, max_char)
print("...Program Executed...")










