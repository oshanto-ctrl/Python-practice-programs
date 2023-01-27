"""
Reverse internal content of every second words in a string.
input: "one two three four five six"
output: "one owt three ruof five xis"
"""

s = "one two three four five six"
l = s.split(' ')
tempL = []

# if else list comprehension approach
[tempL.append(l[i][::-1]) if i&1 else tempL.append(l[i]) for i in range(len(l))]

output = ' '.join(tempL)

print(tempL)
print(output)

