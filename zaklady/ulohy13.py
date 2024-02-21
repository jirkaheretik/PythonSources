def isPalindrom(txt):
    for i in range(len(txt) // 2):
        if txt[i] != txt[len(txt) - 1 - i]:
            return False
    return True

def easyTest():
    print(isPalindrom("radar"))
    print(isPalindrom("oko"))
    print(isPalindrom("okno"))
    print(isPalindrom("jelenovipivonelej"))

def easy():
    print(("Ano, je" if isPalindrom(input("Zadej palindrom:\n")) else "Ne, není") + " to palindrom")

def mid():
    for i in range(32, 256):
        print(f"{i} : {chr(i)}", end="\t")

def bonus():
    print("Zadejte text k zašifrování: ")
    vstup = input()
    print("Zadejte heslo: ")
    heslo = input()
    zasifrovana_zprava = ""
    for idx in range(len(vstup)):
        posun = ord(heslo[idx % len(heslo)]) - ord('a') + 1
        znak = ord(vstup[idx]) + posun
        if znak > ord('z'):
            znak -= 26
        zasifrovana_zprava += chr(znak)
    print(f"Výsledek: {zasifrovana_zprava}")

if __name__ == '__main__':
    #easy()
    #mid()
    bonus()