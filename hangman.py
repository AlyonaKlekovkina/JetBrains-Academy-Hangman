import random
# Write your code here


def check_letter():
    global n, set_to_print
    letter = input("Input a letter: ")
    if letter in the_word:
        if letter in guessed_letters:
            print("No improvements")
            n -= 1
            if n == 0:
                print("You are hanged!")
        else:
            guessed_letters.add(letter)
            set_to_print = set(the_word)
            if len(set_to_print) == len(guessed_letters):
                print("You guessed the word!\nYou survived!")
            else:
                return to_print
    else:
        print("No such letter in the word")
        n -= 1
        if n == 0:
            print("You are hanged!")

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
    set_to_print = set(the_word)
