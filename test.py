# #importing the time module
# import time
#
# #welcoming the user
# #from pip._vendor.distlib.compat import raw_input
#
# name = input("What is your name? ")
#
# print ("Hello, " + name, "Time to play hangman!")
#
# #print ""
# #wait for 1 second
# time.sleep(1)
# print("Start guessing...")
# time.sleep(0.5)
# # here we set the secret
# word = "secret"
#
# # creates an variable with an empty value
# guesses = []
#
# # determine the number of turns
# turns = 10
#
# # Create a while loop
#
# # check if the turns are more than zero
# while turns > 0:
#     failed = 0
#     for char in word:
#         if char in guesses:
#             print(char)
#         else:
#             print("_",)
#             failed += 1
#     if failed == 0:
#         print("You won ")
#             return
#
#
# #ask the user go guess a character
# guess = input("guess a character:")
# # set the players guess to guesses
# guesses += guess
# # if the guess is not found in the secret word
# if guess not in word:
#     turns -= 1
#     print("Wrong")
# print("You have", + turns, 'more guesses')
# if turns == 0:
#     print ("You Lose")


#def nuskaityt(ff='wordlist.txt'):

with open('wordlist.txt', 'r') as wl:
    wordlist = wl.read()
    print(type(wordlist))

# C:\Users\Indre\Desktop\github\KazkasNesvankaus
#nuskaitytt(r'C:\Users\Indre\Desktop\github\KazkasNesvankaus\wordlist.txt')
#with open('failiukas.txt', 'r') as f: #kai atidarinejam per cia visada uzdaro kai baigi
#    failo_duom = f.read()
#    print(type(failo_duom))