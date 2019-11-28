# getting a string from user and printing out
# the list of words that used in string.
# using list comprehensions.

str1 = input('Enter a string and press enter:')
mylist = [letter for letter in str1.split()]
print('The list of your words in string is :\n', mylist)
