"""
Write a program to print the characters 
present at even index and odd index seperately for the given string.
input: "rejoan"
output: even: rja
        odd: eon
"""

s = "rejoan"

# slicing approach
evenIndexChars = s[0::2]
oddIndexChars = s[1::2]

print(f"even: {evenIndexChars}\nodd: {oddIndexChars}")

# looping approach
i = 0
oddCharList = []
evenCharList = []

while i < len(s):
    if not i&1:
        evenCharList.append(s[i])
    else:
        oddCharList.append(s[i])
    i += 1

print(f"even: {''.join(evenCharList)}\nodd: {''.join(oddCharList)}")

        


