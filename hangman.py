import random
# Write your code here


def check_letter():
    global n, set_to_print, letter
    letter = input("Input a letter: ")
    if check_input():
        if letter in the_word:
            if letter in guessed_letters:
                print("You already typed this letter")
            else:
                guessed_letters.add(letter)
                set_to_print = set(the_word)
                if len(set_to_print) == len(guessed_letters):
                    print("You guessed the word {}!\nYou survived!".format(the_word))
                    exit()
                else:
                    return to_print
        else:
            if letter in all_inputted_letters:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                all_inputted_letters.add(letter)
                n -= 1

            if n == 0:
                print("You are hanged!")


def check_input():
    global letter
    if len(letter) != 1 or letter == '':
        print("You should input a single letter")
        return False
    if not letter.islower():
        print("It is not an ASCII lowercase letter")
        return False
    return True


print("H A N G M A N")
while True:
    start_input = input('Type "play" to play the game, "exit" to quit: ')
    if start_input == 'play':
        the_list = ['python', 'java', 'kotlin', 'javascript']
        the_word = random.choice(the_list)
        guessed_letters = set()
        all_inputted_letters = set()
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
        continue
    elif start_input == 'exit':
        break
