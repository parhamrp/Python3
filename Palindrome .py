def palindrome(MyString):
	first_half, second_half = MyString.lower()[:int(len(MyString)/2)]\
	, MyString.lower()[int(len(MyString)/2):]
	return first_half == second_half[::-1]


print(palindrome('helleh'))
print(palindrome('8008'))
