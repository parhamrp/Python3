# #  getting integer value from user and calculate
# #  factorial of the number. using 'for' loop.
# #  getting value from user.
# _promt_value_ = int(input('enter an intger number to calculate the factorial:'))
# #  initialize the first value.
# final_value = 1
# for item in range(1, _promt_value_ + 1):
#       final_value = final_value * item
# #   print final calculation      
# print ('Factorial of ',_promt_value_, 'is:', final_value)


# #  getting integer value from user and calculate
# #  factorial of the number. using 'while' loop.
# #  getting value from user.
# input_value = input('enter an intger number to calculate the factorial:')
# _promt_value_ = int (input_value)
# _copy_of_promt_ = str(input_value)
# #  initialize the first value.
# initial_value = 1
# if _promt_value_ < 0:
#       print('The number you entered is less than 0.')
# elif _promt_value_ == 0:
#       print (_copy_of_promt_+'!','  is: 1')
# else:
#       while _promt_value_ > 0:
#             initial_value = initial_value * _promt_value_
#             _promt_value_ -= 1

#       #   print final calculation      
#       print (_copy_of_promt_+'!','  is:', initial_value)




# _promt_value_ = int(input('enter an intger number to calculate the factorial:'))
# _copy_of_promt_ = str(_promt_value_)
# #  initialize the first value.
# initial_value = 1
# if _promt_value_ < 0:
#       print('The number you entered is less than 0.')
# break 
# elif (_promt_value_ == 0):
#      print (_copy_of_promt_+'!','  is: 1')
# else:
#       for item in range (1, _promt_value_ +1):
#             initial_value = initial_value * item

#       #   print final calculation      
#       print (_copy_of_promt_+'!','  is:', initial_value)
            
# def factorial_func(any_number):
#       initial_value = 1
#       if any_number < 0:
#             continue
#       elif any_value
#       for 



























# input_value  = int(input('enter a number:'))
# copy_of_prompt = str(input_value)
# flag = False
# while not flag:
#       if input_value < 0:
#             print ('the number that you entered is less than zero!')
#             input_value = int(input('enter a number:'))
#             flag = True
#       elif input_value == 0:
            


any_number = int(input('enter an integer number:'))
initial_value = 1
while any_number < 0:
      print ('input is less than zero!')
      any_number = int(input('enter a bigger number than zero:'))

if  any_number == 0:
      print('0! is 1')
            
else: 
      copy_of_value = str(any_number)
      for item in range (1, any_number+1):
            initial_value = initial_value * item
      print (copy_of_value+'!','is',initial_value)


      




























