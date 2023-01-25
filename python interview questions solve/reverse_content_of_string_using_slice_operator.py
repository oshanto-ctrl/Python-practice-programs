input_string = "AMD-RADEON-GRAPHICS"

# using slice operator  &[begin:end:step]
reverse_with_slice = input_string[::-1]
print(reverse_with_slice)

# using reversed(). returns reverse object
reverse_with_inbuilt_reversed = reversed(input_string)
output_string = ''.join(reverse_with_inbuilt_reversed)
print(output_string)

# using while loop to reverse
out_string = ''
i = len(input_string) - 1

while i >= 0:
    out_string += input_string[i]
    i -= 1

print(out_string)





