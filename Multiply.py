# Write a Python function to multiply all the numbers in a list.

def multiply(lst):
	total = 1
	for item in lst:
		total *= item
		# total = lst[item] * lst[item+1]
	return total

	
# print(multiply([1,2,4,-3,3]))