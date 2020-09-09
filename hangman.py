import random
# Write your code here
print("H A N G M A N")
the_list = ['python', 'java', 'kotlin', 'javascript']
the_word = random.choice(the_list)
first_letters = the_word[:3]
last_letters = the_word[3:]
replacement = first_letters + len(last_letters) * '-'

the_guess = input("Guess the word {}: ".format(replacement))
if the_word == the_guess:
    print("You survived!")
else:
    print("You are hanged!")
