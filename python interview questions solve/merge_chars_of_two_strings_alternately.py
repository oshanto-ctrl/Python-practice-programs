"""
input:
s1 = "LAMP"
s2 = "JUMP"

output:
out = "LJAUMMPP"
"""
s1 = "LAMP"
s2 = "JUMP"
out = ""

# method 1
i, j = 0, 0

while i < len(s1) or j < len(s2):
    out += s1[i] + s2[j]
    i += 1
    j += 1

print(out)

# method 2

s = ""
m = max(len(s1), len(s2))
i = 0
while(i < m):
    s += s1[i] + s2[i]
    i += 1
print(s)