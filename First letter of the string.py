# getting a string from user and print out
# the first letter of the string
str1 = input("enter a string and then press enter:")
mylist = [letter[0] for letter in str1.split()]
print ('the list of the first letter is :', "\n", mylist)
