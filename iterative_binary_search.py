__author__ = "Rejoan"

"""
Iterative approach of binary search.
TC: O(log n)
"""

def binary_search(l, low, high, key):
    """
    binary_search() searches key in a list
    returns the index of the key if found,
    else returns -1.
    """

    while low <= high:
        mid = low + (high - low) // 2
        guess = l[mid]  # guess is middle key in the list

        if guess == key:
            return mid
        elif guess > key:
            high = mid - 1
        else:
            low = mid + 1

    # if not found return -1
    return -1 

# driver
# a sorted numeric list
l = [-1, 0, 1, 2, 3, 10, 12, 19, 21, 27, 31, 33, 37, 90, 100] 
key = 31  # search for this element

low = 0
high = len(l) - 1

bs1 = binary_search(l, low, high, key)  # calling the function

if(bs1 != -1):
    print(f"Key {key} found at index {bs1} in the list.")
else:
    print(f"{key} is not in the list.")

print("...Program Finished...")