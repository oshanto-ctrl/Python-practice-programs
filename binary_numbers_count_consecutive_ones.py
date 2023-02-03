"""
Decimal number input, 
convert to binary,
count the maximum numbers of consecuitive 1's
print the result.
"""
# n = int(input()).strip()
n = 5
one_number = bin(n)[2:].split('0')
print(one_number)
a = bin(n).replace("0b", "")
print(a)

result = max([len(number) for number in one_number])
print(result)
