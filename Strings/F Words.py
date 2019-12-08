# getting a string from user and if
# a word start with 'F or f', print out the word!

strf = input('Enter a string and then press enter:')
for word in strf.split():
    if word[0].lower() == 'f':
        print ('The word is :', word)
        
