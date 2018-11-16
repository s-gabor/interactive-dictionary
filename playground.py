# playground.py

import constants
import json
from difflib import get_close_matches

print('This is an english dictionary.')

dictionary = json.load(open(constants.fname, 'r'))
while True:
    word = input('Enter a word("q" to exit the program): ')
    if word == 'q':
        break
    output = None
    if word in dictionary:
        pass
    elif word.capitalize() in dictionary:
        word = word.capitalize()
    elif word.lower() in dictionary:
        word = word.lower()
    elif word.upper() in dictionary:
        word = word.upper()
    else:
        closest_word = get_close_matches(word, dictionary, n=1, cutoff=0.6)
        if closest_word:
            confirmation = input(f'I\'m not familiar with that word. Did you mean "{closest_word[0]}" instead(y/n)? ')
            if confirmation[0] in 'Yy':
                word = closest_word[0]
            else:
                output = 'Sorry I couldn\'t be more helpful.'
        else:
            output = 'That\'s not an english word! Try again.'

    if output:
        print(output)
    else:
        output = dictionary[word]
        if len(output) == 1:
            print(f'"{word}":')
            print(f'   {output[0]}')
            print()
        else:
            print(f'"{word}" has multiple meanings:')
            for i in range(1, len(output)+1):
                print(f'   {i}.', output[i-1])
            print()
print('Thanks! Have a nice day.\n')
