
import random


def random_cislicko():
    return random.randint(1000, 9999)


def gud_positiiiiion(tajno, guuus):
    pocet = 0
    for i in range(4):
        if tajno[i] == guuus[i]:
            pocet += 1
    return pocet


def bad_positiiiiion(tajno, guess):
    pocet = 0
    for digit in guess:
        if digit in tajno and tajno.index(digit) != guess.index(digit):
            pocet += 1
    return pocet


def main():
    tajny_cislickoo = str(random_cislicko())
    kus = 0
    print(f"tajny cisliscko: {tajny_cislickoo}")

    while True:
        gus = input("pokus: ")
        kus += 1

        if len(gus) != 4 or not gus.isdigit():
            print("4 cislice chci ")
            continue

        gud_pozice = gud_positiiiiion(tajny_cislickoo, gus)
        bad_pozice = bad_positiiiiion(tajny_cislickoo, gus)

        if gus == tajny_cislickoo:
            print(f"cislo: {tajny_cislickoo} jsi uhadnul v  {kus} pokusech")
            break
        else:
            print(f"spravne uhodnutych: {gud_pozice}")
            print(f"na spatne pozici: {bad_pozice}")


main()