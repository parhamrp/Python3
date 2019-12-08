# getting a number from user and print out
# all numbers from 1 to that special number that are 
# divisible to 3 but first we will check if number is greater than 0.
print('Enter an integer number to count all numbers between 1 \
and your number, which they are divisible to 3. ')
user_number = int(input('Enter an integer number then press enter:'))
while user_number <= 0:
    user_number = int(input('Enter an integer number, greater than 0:'))
for number in range (1 , user_number + 1):
    if number % 3 == 0:
        print (str(number)+' is divisible to 3.')
    else:
        print (number)
