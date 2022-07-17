__author__ = "Rejoan"

"""
This program checks if
a integer number is palindrome or not.
__author__ = "Rejoan"
"""

class Palindrome():
    """Modeling a palindrome checker."""

    def __init__(self, number):
        """Initialize Palindrome's attributes."""
        self.number = number

    def check_palindrome(self):
        """
        If palindrome evaluates true then check_palindrome()
        returns Ture, else return False
        """
        checker = False
        num_in_str = str(self.number)  # converts the number in string
        str_in_reverse = reversed(num_in_str)  # reverses the number converted in string
        if list(num_in_str) == list(str_in_reverse):
            checker = True
        else:
            checker = False

        return checker  # returns the boolean state

# Driver
word_one = Palindrome(11122111)
check_word_one = word_one.check_palindrome()  # Expects True
if check_word_one:
    print(f"Yes, It is palindrome.")
else:
    print(f"No, It is not palindrome")

print("...Program Finished...")












