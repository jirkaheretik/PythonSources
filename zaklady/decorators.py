def d1(fn):
    print("D1 načteno")
    def _f():
        print("D1 spuštěno")
        fn()
        print("D1 ukončeno")
    return _f

def d2(fn):
    print("D2 načteno")
    def _f():
        print("D2 spuštěno")
        fn()
        print("D2 ukončeno")
    return _f

@d1
@d2
def f():
    print("Vlastní volání funkce")

print("zde třeba dlouho běží hlavní program...")
for _ in range(10):
    print(" a běží...")
print("Až se jednou zavolá funkce:")
f()
print("A znovu běží program a třeba zase zavolá naši dekorovanou funkci:")
f()
print("Zatímco načtení už znovu neprobíhá, samotné dekorátory (obsah) jsou spouštěny znovu a znovu")
print("Vždy v pořadí od vnějších k vnitřním, pak samotná funkce. Ještě jednou:")
f()