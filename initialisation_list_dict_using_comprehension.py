# List of cubes from 0 to n^3
n = 5
cubed_numbers = [i ** 3 for i in range(n + 1)]
print(cubed_numbers)

# Initialise a list of n to 0 using list comprehension
arr  = [0 for _ in range(n)] # expected [0, 0, 0, 0, 0]
print(arr) # OK

# Initialise counters for the letters in a string
# expected: {'h': 0, 'e': 0, 'l': 0, 'o': 0, ' ': 0, 'w': 0, 'r': 0, 'd': 0}
input_string = "hello world"
input_string_occurences = {letter: 0 for letter in input_string} # dictionary will generate
print(input_string_occurences) # OK




