# Write a Python function that takes a list and 
# returns a new list with unique elements of the first list.
def unique_list (lst):
	var = set(lst)
	myList = [item for item in var]
	# for item in var:
	# 	myList.append(item)
	return myList

# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
