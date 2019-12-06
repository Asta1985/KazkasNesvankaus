import random
import sys

wordList = [
"liutas", "sketis", "langas", "kompiuteris", "stiklas", "stogas", "laiptai", "desktop",
 "kaledos", "katinas", "kobra", "citrina", "obuolys", "sninga", "lova"
           ]

guess_word = []
secretWord = random.choice(wordList) # lets randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def beginning():
    print("Labukas!\n")

    while True:
        name = input("Kuo tu vardu?\n").strip()

        if name == '':
            print("Taip negalima! Jokiu tusciu eiluciu :)")
        else:
            break

beginning()

def newFunc():
    print("Manau puikus metas pazaisti kartuves!\n")
    while True:
        gameChoice = input("Ar zaidziam?\n").upper()
        if gameChoice == "Taip" or gameChoice == "T":
            break
        elif gameChoice == "Ne" or gameChoice == "N":
            sys.exit("Kaip gaila... Na - geros dienos!")
        else:
            print("Prasome ivesti tik T arba N")
            continue

newFunc()



def change():
    for character in secretWord:
        guess_word.append("-")
    print("Zodis kuri reikia atspeti turi", length_word, "raides")
    print("galima ivesti tik raides nuo a-z\n\n")
    print(guess_word)



def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Spek raide\n").lower()
        if not guess in alphabet:
            print("raide reikia rinktis nuo a iki z is ne lietuvisku raidziu")
        elif guess in letter_storage:
            print("Sita raide jau spejai!")
        else:
            letter_storage.append(guess)
            if guess in secretWord:
                print("Atspejai!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)
                if not '-' in guess_word:
                    print("Laimejai!")
                    break
            else:
                print("Sios raides nera zodyje. Spek dar karta!")
                guess_taken += 1
                if guess_taken == 10:
                    print("Deja pralaimejai... :<! Zodis buvo",         secretWord)

change()
guessing()

print("Zaidimo pabaiga!")