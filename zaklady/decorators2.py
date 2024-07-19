import time


def zmer_cas(znacka):
    def decorator(function):
        def _f():
            zacatek = time.time()
            function()
            konec = time.time()
            print(f"{znacka}: {konec - zacatek:.5f} s", end="")
        return _f
    return decorator


def dekoruj(znacka):
    def decorator(function):
        def _f():
            print(znacka, end="")
            if znacka == "/":
                time.sleep(0.5)
            function()
            if znacka == "/":
                time.sleep(0.5)
            print(znacka, end="")
        return _f
    return decorator


@zmer_cas(znacka="Vnější")
@dekoruj(znacka="/")
@zmer_cas(znacka="Střední")
@dekoruj(znacka="-")
@dekoruj(znacka="*")
@zmer_cas(znacka="Vnitřní")
def f():
    time.sleep(1)
    print("Vlastní volání funkce")

f()
print()
f()