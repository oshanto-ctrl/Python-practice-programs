"""
Slicing operations in a list and most important methods of a list for our usage like len(), count(), pop(), append() etc
"""

# A list of fruits
fruits = ["Apple", "Banana", "Apricot", "Atemoya", "Avocados", "Blueberry", "Blackcurrant", "Ackee","Cranberry", "Cantaloupe", "Cherry"]

i = 4
# the ith element of fruits list
print(fruits[i]) # Avocado
# L[i:j] the list of fruit with indices starting with i upto (not including) j
print(fruits[1:4]) # [Banana, Apricot, Atemoya]
j = 6
# first j fruits from fruits list
print(fruits[:j]) # [Avocado, ... , Blueberry]
# All the fruits from ith onwards
print(fruits[i:]) # [Avocad, ... , Cherry]

i = 0; j = 8; k = 2
# fruits[i:j:k] fruits from the ith up to (not including) jth taking only every kth fruit
print(fruits[i:j:k]) # [Apple, Apricot, Avocados, Blackurrant]

# every fruits in the list with event indices
print(fruits[::2])

# reverse 'copy' of the fruit list
print(fruits[::-1])

"""
A function has constant amortised complexity if, for several successive calls to it,
the average complexity is constant, even if some of these calls take a time linear in n.
"""

# Number of fruits in the fruits list using len(): O(1)
print("Amount of Fruits in the bucket = ", len(fruits))


# Returns Sorted Copy of the fruits list (Do not modifies the list): O(n log n)
print("Before sort using sorted() = ", fruits)
print("After sorting using sorted() = ", sorted(fruits))

# Sorts fruits list in place using .sort() (permanently): O(n log n)
print("Before sort using fruits.sort() = ", fruits)
fruits.sort()
print("After sort using fruits.sort() = ", fruits)
print("Current formation of fruits list = ", fruits)

# Append a fruit to the end of the fruit list using append(x): amortised O(1)
fruits.append("Jack-fruit")
fruits.append("Mango")
fruits.append("Apple")
fruits.append("Watermelon")
# print(fruits)

# Pop the last fruit from the fruits list using pop(): amortised O(1)
fruits.pop() # Watermelon from the fruits list will be poped. 
# print(fruits)


# count the number of occurences of a fruit in fruits list using .count(item): O(n)
search_item = "Apple"
apple_counter = fruits.count(search_item) # returns 2
print(apple_counter)

# Check if any fruit found in the list or not using fruit_name in fruits list: O(n)
# check if 'Banana' in the list
print('Banana' in fruits) # Evaluate and prints True
# check with a misspell of 'Banana' as 'bananaa'
print('bananaa' in fruits) # Evaluates and prints False

# :) Thank you #

