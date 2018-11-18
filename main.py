# main.py

import utils


utils.intro_message()
user_input = input('Enter a word("q" to exit the program): ')

while user_input != 'q':
    utils.translate(user_input)
    user_input = input('Enter another word("q" to exit the program): ')

utils.exit_message()
