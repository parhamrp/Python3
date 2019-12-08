################### Sample Solution ###################
n = int(input("Please enter a positive integer: "))
if n > 1:
    print (n*"*") # Print the top line
    for x in range(n-1, 1, -1):
        print("*"+ (x-2)*" "+"*") # Print the middle lines
    print("*") #print the bottom line
elif n == 1:
    print("*")
    
