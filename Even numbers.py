# getting a number from user and print out
# all even numbers from 1 to that special number
# but first we will check if number is greater than 0.
print('Enter an integer number to count all even numbers between 1\
and your number. ')
user_number = int(input('Enter an integer number then press enter:'))
while user_number <= 0:
    user_number = int(input('Enter an integer number, greater than 0:'))
for number in range (1 , user_number + 1):
    if number % 2 == 0:
        print ('Even number is '+ str(number))
    else:
        print (number)
