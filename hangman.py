import random
# Write your code here


def check_letter():
    letter = input("Input a letter: ")
    if letter in the_word:
        guessed_letters.add(letter)
        return to_print
    else:
        print("No such letter in the word")


print("H A N G M A N")
the_list = ['python', 'java', 'kotlin', 'javascript']
the_word = random.choice(the_list)
guessed_letters = set()
n = 8
while n > 0:
    to_print = ''

    for i in the_word:
        if i in guessed_letters:
            to_print += i
        else:
            to_print += '-'

    print("\n", to_print, sep="")

    check = check_letter()
    n -= 1
    if n == 0:
        print("\nThanks for playing!\nWe'll see how well you did in the next stage")
