""" 
Write a Program To REVERSE order of words present in the given string.
Input: "I have a pen"
Output: "pen a have I"
"""
s = "I have a pen"
print("Input string: ", s)

# Using loops and lists
L = list(s.split(' '))
ss = " "
# print(L)
REV_L = []
while len(L) > 0:
    word = L[-1]
    # print("W = ", word)
    REV_L.append(word)
    L.pop()

# print(REV_L)
print("Output string: ", ss.join(REV_L))




