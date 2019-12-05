def up_low(myString):
	Cqty = 0
	Lqty = 0
	for letter in myString:
		if letter.isupper():
			Cqty += 1
		if letter.islower():
			Lqty += 1
	print ('No. of Upper case characters:',Cqty)
	print ('No. of Lower case characters:',Lqty)

# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)
