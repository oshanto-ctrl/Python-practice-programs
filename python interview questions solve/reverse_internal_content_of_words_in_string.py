""" 
Write a Program To REVERSE the content of words present in the given string.
Input: "A good Book"
Output: "A doog kooB"
"""
s = "A good Book"

# split s and convert to a list
l = s.split()
tempL = [] # empty list
"""
for w in l:
    tempL.append(w[::-1])
"""
[tempL.append(w[::-1]) for w in l]

output = ' '.join(tempL) # Joins as a string
print(output)


