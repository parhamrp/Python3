# A functiom to check if a string is panagram or not!
# panagram function.

def ispangram(mystring):
	'''
	PANAGRAM FUNCTION 
	INPUT: A STRING
	OUTPUT: BOOLEAN VALUE (TRUE/FALSE)
	INFO: This function takes a string and check the string 
	is panagram or not (panagram string has all english alphabets.)
	'''
	# calling string library to import 'string.ascii.lowercase'
	# so the function imports string library as we use it.
	import string
	# Save all alphabet into 'allchar'
	allchar = list(string.ascii_lowercase)
	# remove all whitspaces in mystring and turn all it's
	# alphabet into lowercase.
	final_str = ''.join(mystring.lower().split())
	# make a unique list of characters in mystring.
	unique_char = list(set(final_str))
	# sort all alphabets from a to z.
	unique_char.sort()
	# print(unique_char)
	# returning final result which is panagram or not(True/False).
	return unique_char == allchar



# print(ispangram('The quick brown fox jumps over the lazy dog'))


