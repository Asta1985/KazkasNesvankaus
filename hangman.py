import random
import sys

zodziu_sar = ['xii'
    #"liūtas", "skėtis", "langas", "kompiuteris", "stiklas", "stogas", "laiptai", "ekranas",
    # "kalėdos", "katinas", "šuo", "citrina", "obuolys", "sninga", "lova", "česnakas"
]  # kaip padaryt kad iseitu uploadint wordlist


class Zaidimas:
    speti_zodi = []
    slaptas_zod = random.choice(zodziu_sar)
    zodzio_ilgis = len(slaptas_zod)
    alphabet = "aąbcčdeėęfghiįjklmnopqrsštųuūvwxyzž"
    zodziu_talp = []

    def anuliuoti(self):
        self.speti_zodi = []
        self.zodziu_talp = []
        self.slaptas_zod = random.choice(zodziu_sar)

    def beginning(self):
        print("Labukas!\n")
        while True:
            name = input("Kuo tu vardu?\n").strip()
            if name == '':
                print("Taip negalima! Jokių tuščių eilučių :)")
            else:
                break

    def pakartot(self, zinute):  # "Gal pabandom dar kart?\n"
        print(zinute)
        while True:
            gameChoice = input("Ar žaidžiam?\n").upper()
            if gameChoice == "TAIP" or gameChoice == "T":
                break
            elif gameChoice == "NE" or gameChoice == "N":
                sys.exit("Kaip gaila... Na - geros dienos!")
            else:
                print("Prašome įvesti tik Taip arba Ne")
                continue

    def change(self):
        for _ in self.slaptas_zod:
            self.speti_zodi.append("-")
        print("Žodis kuri reikia atspėti turi", self.zodzio_ilgis, "raides")
        print("galima ivesti tik raides nuo a iki ž\n\n")
        print(self.speti_zodi)

    def guessing(self):
        guess_taken = 1
        while guess_taken < 10:
            guess = input("Spėk raide\n").lower()
            if guess not in self.alphabet:
                print("raidę reikia rinktis nuo a iki ž su lietuviškom raidėm")
            elif guess in self.zodziu_talp:
                print("Šitą raidę jau spėjai!")
            else:
                self.zodziu_talp.append(guess)
                if guess in self.slaptas_zod:
                    print("Atspėjai!")
                    for x in range(0, self.zodzio_ilgis):
                        if self.slaptas_zod[x] == guess:
                            self.speti_zodi[x] = guess
                    print(self.speti_zodi)
                    if '-' not in self.speti_zodi:
                        print("Laimėjai!")
                        self.anuliuoti()
                        break
                else:
                    print("Šios raidės nėra žodyje. Spėk dar kartą!")
                    guess_taken += 1
                    if guess_taken == 10:
                        print("Dėja pralaimėjai... :(! Žodis buvo", self.slaptas_zod)


if __name__ == '__main__':
    zaidimas = Zaidimas()
    zaidimas.beginning()
    zaidimas.pakartot("Manau puikus metas pažaisti kartuves!\n")
    zaidimas.change()
    zaidimas.guessing()
    # kaip padaryt kad vel pradetu nuo zodzio ar zaisim dar karta?
    zaidimas.pakartot("Gal pabandom dar kart?\n")
    zaidimas.change()
    zaidimas.guessing()  # ir tada neveikia nes pirmame zaidime rinktos raides jau kartojasi
    print("Žaidimo pabaiga!")
