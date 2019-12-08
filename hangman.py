import random
import sys

zodziu_sar = [
"liūtas", "skėtis", "langas", "kompiuteris", "stiklas", "stogas", "laiptai", "ekranas",
 "kalėdos", "katinas", "šuo", "citrina", "obuolys", "sninga", "lova", "česnakas"
           ]  # kaip padaryt kad iseitu uploadint wordlist

speti_zodi = []
slaptas_zod = random.choice(zodziu_sar)
zodzio_ilgis = len(slaptas_zod)
alphabet = "aąbcčdeėęfghiįjklmnopqrsštųuūvwxyzž"
zodziu_talp = []

def beginning():
    print("Labukas!\n")
    while True:
        name = input("Kuo tu vardu?\n").strip()
        if name == '':
            print("Taip negalima! Jokių tuščių eilučių :)")
        else:
            break

beginning()

def newFunc():
    print("Manau puikus metas pažaisti kartuves!\n")
    while True:
        gameChoice = input("Ar žaidžiam?\n").upper()
        if gameChoice == "Taip" or gameChoice == "T":   #neveikia su taip
            break
        elif gameChoice == "Ne" or gameChoice == "N":
            sys.exit("Kaip gaila... Na - geros dienos!")
        else:
            print("Prašome įvesti tik T arba N")
            continue

newFunc()



def change():
    for character in slaptas_zod:
        speti_zodi.append("-")
    print("Žodis kuri reikia atspėti turi", zodzio_ilgis, "raides")
    print("galima ivesti tik raides nuo a iki ž\n\n")
    print(speti_zodi)



def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Spėk raide\n").lower()
        if not guess in alphabet:
            print("raidę reikia rinktis nuo a iki ž su lietuviškom raidėm")
        elif guess in zodziu_talp:
            print("Šitą raidę jau spėjai!")
        else:
            zodziu_talp.append(guess)
            if guess in slaptas_zod:
                print("Atspėjai!")
                for x in range(0, zodzio_ilgis):
                    if slaptas_zod[x] == guess:
                        speti_zodi[x] = guess
                        print(speti_zodi)
                if not '-' in speti_zodi:
                    print("Laimėjai!")
                    break
            else:
                print("Šios raidės nėra žodyje. Spėk dar kartą!")
                guess_taken += 1
                if guess_taken == 10:
                    print("Dėja pralaimėjai... :(! Žodis buvo", slaptas_zod)

change()
guessing()  #kaip padaryt kad vel pradetu nuo zodzio ar zaisim dar karta?


def pakartot():
    print("Gal pabandom dar kart?\n")
    while True:
        gameChoice = input("Ar žaidžiam?\n").upper()
        if gameChoice == "Taip" or gameChoice == "T":
            break
        elif gameChoice == "Ne" or gameChoice == "N":
            sys.exit("Kaip gaila... Na - geros dienos!")
        else:
            print("Prašome įvesti tik T arba N")
            continue

pakartot()

print("Žaidimo pabaiga!")