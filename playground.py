# playground.py

import constants

print('This is an english dictionary.')

dictionary = constants.data
while True:
    word = input('Enter a word("q" to exit the program): ')
    if word == 'q':
        break
    if word in dictionary:
        print(dictionary[word])
    else:
        print('That\'s not an english word. Try again!')
print('Thanks! Have a nice day.\n')
