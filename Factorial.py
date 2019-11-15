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