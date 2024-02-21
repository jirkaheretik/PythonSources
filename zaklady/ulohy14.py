
def easy():
    print("Výpočet průměru známek")
    print("Zadejte známky oddělené čárkou: ")

    vstup = input().split(",")
    soucet = 0
    for znamka in vstup:
        soucet += int(znamka.strip())
    print(f"Průměr: {soucet/len(vstup)}")

def mid():
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                      "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                      ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    print("Zadejte zprávu k zakódování: ")
    puvodni_zprava = input().lower()
    zasifrovana_zprava = ""
    for znak in puvodni_zprava:
        if znak in abeceda:
            zasifrovana_zprava += morseovy_znaky[abeceda.index(znak)] + " "
    print(f"Zakódovaná zpráva: {zasifrovana_zprava}")

def bonus():
    smiles = [":)", ":D", ":P"]
    forSmileys = ".?!"
    idx = 0
    print("Zadej text k rozveselení: ")
    text = input()
    result = ""
    for znak in text:
        if znak != ".":
            result += znak
        if znak in forSmileys:
            result += " " + smiles[idx % len(smiles)]
            idx += 1
    print(f"Rozveselený text: {result}")

if __name__ == '__main__':
    #easy()
    #mid()
    bonus()