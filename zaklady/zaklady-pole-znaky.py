DNY = ["neděle", "pondělí", "úterý", "středa", "čtvrtek", "pátek", "sobota"]
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def den_v_tydnu(poradi, dny = DNY):
    return dny[poradi % len(dny)]

def obrat_text_cyklem(text):
    vysledek = ""
    for i in range(len(text), 0, -1):
        vysledek += text[i - 1]
    return vysledek

def obrat_text(text):
    znaky = list(text)
    znaky.reverse()
    return "".join(znaky)

def prumer_platu(text):
    platy = text.split(",")
    suma = 0
    for plat in platy:
        suma += int(plat.strip())
    return suma / len(platy)

def soucet_cifer_v_retezci(text):
    suma = 0
    for index in range(len(text)):
        cislo_znaku = ord(text[index])
        if cislo_znaku >= 48 and cislo_znaku <= 57:
            suma += cislo_znaku - 48
    return suma

if __name__ == '__main__':
    val = 4
    print(den_v_tydnu(val))
    print(den_v_tydnu(val, ["a", "b", "c"]))
    print(den_v_tydnu(val, DAYS))
