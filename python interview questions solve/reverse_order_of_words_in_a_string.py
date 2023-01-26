""" 
Write a Program To REVERSE order of words present in the given string.
Input: "I have a pen"
Output: "pen a have I"
"""
s = "I have a pen"
print("Input string: ", s)

# Approach using loops and lists
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


# Approach with less line of code
l = s.split() # s splits and converts to list of words
rev_l = l[::-1] # reverse the word order of list l and store in another list 
final_string = ' '.join(rev_l) # join the word contents with a space in a output string
print("Output string2: ", final_string)

if ss == final_string:
    print("Both are same.")
else:
    print("Both are not same, something Fishy!") # reason is the output varibales (ss, final_str)
    # have different way of concating (joining) the words.

