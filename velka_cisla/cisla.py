from pathlib import Path
e = Path('e.txt').read_text()
f = Path('f.txt').read_text()
p = Path('p.txt').read_text()

delka_podretezce = 7
pocet_desetinnych_mist = 999994

vysledky = []
for i in range (0, pocet_desetinnych_mist):
    if e[i:i+3] == "157" or e[i:i+3] == "158" or e[i:i+3] == "504":
        hledam = e[i:i+delka_podretezce]
        if hledam in f and hledam in p:
            #print(f"Nalez retezec '{hledam}'")
            # ? break
            vysledky.append(hledam)

vysledky.sort()
print(vysledky)
