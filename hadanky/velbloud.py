import math

"""
Idea: mam X bananu (vstup 1) v miste A, chci je dostat do mista B vzdaleneho Y (vstup 2) a k dispozici
je velbloud, ktery unese Z bananu najednou (vstup 3) a zere Q bananu (vstup 4) na jednotku
Defaults: 3000, 1000, 1000, 1
"""
def velbloudi(banany, vzdalenost, nosnost, cena):
    zadani = "{} bananu prevezt na vzdalenost {} velboudem o nosnosti {}, ktery skrmi {} banan(u) na km".format(banany, vzdalenost, nosnost, cena)
    while vzdalenost > 0:
        # udelej krok:
        vzdalenost -= 1
        # POZOR ne vzdy se chci vracet pro vsechny banany, zalezi na cene:
        zbytek = banany % nosnost
        if zbytek > 0 and 2 * cena >= zbytek:
            # nema cenu se pro vsechny vracet
            print("DBG. Bananu: {}, vzdalenost: {}, zahazuji (snim) {} banan(y)".format(banany, vzdalenost, zbytek))
            banany -= zbytek
        if banany > 0:
            banany -= (2 * math.ceil(banany/nosnost) - 1) * cena
        if banany <= 0:
            print("Uloha nema reseni, konec ve vzdalenosti " + str(vzdalenost))
            exit(0)
        #print("Mezikrok - {} bananu, vzdalenost {}".format(banany, vzdalenost))
    print("Uloha '{}' ma reseni: {} bananu lze dopravit do cile.".format(zadani, banany))

def velbloudi2(banany, vzdalenost, nosnost, cena):
    zadani = "{} bananu prevezt na vzdalenost {} velboudem o nosnosti {}, ktery skrmi {} banan(u) na km".format(banany, vzdalenost, nosnost, cena)
    while vzdalenost > 0:
        # spec. pripad: mame se vracet i pro posledni davku?
        zbytek = banany % nosnost
        if zbytek > 0 and 2 * cena >= zbytek:
            # nema cenu se pro vsechny vracet
            print("DBG. Bananu: {}, vzdalenost: {}, zahazuji (snim) {} banan(y)".format(banany, vzdalenost, zbytek))
            banany -= zbytek
        # udelat krok:
        cenaZaKm = (2 * math.ceil(banany/nosnost) - 1) * cena
        vzdalenost -= 1
        banany -= cenaZaKm
        # uz to dojedeme?
        if banany <= nosnost:
            # to uz umime, nalozit a jet, lze rozhodnout, co dal:
            diff = banany - vzdalenost * cena
            if diff >= 0:
                print(f"Do cile dovezeme {diff} bananu")
            else:
                vzdalenost -= banany//cena
                print("Uloha nema reseni, skoncime {} km od cile.".format(vzdalenost))
            break # ukoncit cyklus


velbloudi2(3468, 1000, 1000, 2)
#velbloudi(10000, 1000, 1000, 2)