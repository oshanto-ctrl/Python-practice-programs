__author__ = "Rejoan"

"""
Recursive approach of binary search.
TC: O(log n)
"""

def binary_search(l, low, high, key):
    """
    binary_search() searches key in a list
    returns the index of the key if found,
    else returns -1.
    """

    if low <= high:
        mid = low + (high - low) // 2

        if l[mid] == key:
            return mid
        elif l[mid] < key:
            return binary_search(l, mid+1, high, key)
        else:
            return binary_search(l, low, mid-1, key)

    else:
        return -1  # If key not found in the list 

# driver
# a sorted numeric list
l = [-1, 0, 1, 2, 3, 10, 12, 19, 21, 27, 31, 33, 37, 90, 100] 
key = -1  # search for this element

low = 0
high = len(l) - 1

b1 = binary_search(l, low, high, key)  # calling the function

if(b1 != -1):
    print(f"Key {key} found at index {b1} in the list.")
else:
    print(f"{key} is not in the list.")

print("...Program Finished...")
