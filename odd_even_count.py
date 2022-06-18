__author__ = "Rejoan"

def odd_even_counter(arr, len_of_arr):
	"""
	Counts occurence of odd and
	evens in an array.
	"""	
	odd_count, even_count = 0, 0
	for i in range(0, len_of_arr):
		if(arr[i] & 1):
			odd_count += 1
		else:
			even_count += 1

	# return the counts
	return odd_count, even_count


# driver
arr = [1, 8, 3, 10, -1, 0, -2]
len_of_arr = len(arr)

# print(odd_even_counter(arr, len_of_arr))
odds, evens = odd_even_counter(arr, len_of_arr)

print(f"odds = {odds} evens = {evens}")  # expected output : odds = 3 evens = 4

print("...Program Finished...")
