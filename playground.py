# playground.py

import constants
from difflib import get_close_matches

print('This is an english dictionary.')

dictionary = constants.data
while True:
    word = input('Enter a word("q" to exit the program): ')
    if word == 'q':
        break
    if word in dictionary:
        print(dictionary[word])
    else:
        closest_word = get_close_matches(word, dictionary, n=1, cutoff=0.6)
        if closest_word:
            confirmation = input(f'I\'m not familiar with that word. Did you mean "{closest_word[0]}" instead(y/n)? ')
            if confirmation[0] in 'Yy':
                print(dictionary[closest_word[0]])
            else:
                print('Sorry I couldn\'t be more helpful.')
        else:
            print('That\'s not an english word! Try again.')
print('Thanks! Have a nice day.\n')
