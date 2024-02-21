

def easy():
    for r in range(8):
        for c in range(8):
            print(" " if (r + c) % 2 else "█", end="")
        print()

def mid():
    print("Číslo v desítkové soustavě:")
    cislo = int(input())
    print("Číselná soustava (2-16):")
    base = int(input())
    print(f"Číslo ve zvolené soustavě: {toBase(cislo, base)}")

def toBase(cislo, base):
    znaky = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while (cislo > 0):
        res = znaky[cislo % base] + res
        cislo //= base
    return res


def bonus():
    cisla = input("Zadej čísla pro seřazení (oddělená čárkou): ")
    arr = []
    for c in cisla.split(","):
        arr.append(int(c.strip()))
    selectionSort(arr)
    print("Seřazená čísla:")
    print(", ".join(map(str, arr)))

def bubbleSort(arr):
    swap = True
    while swap:
        swap = False
        for idx in range(len(arr) - 1):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swap = True

def selectionSort(arr):
    sorted = 0
    while sorted < len(arr):
        minidx = sorted
        for idx in range(sorted + 1, len(arr)):
            if arr[idx] < arr[minidx]:
                minidx = idx
        if minidx != sorted:
            arr[sorted], arr[minidx] = arr[minidx], arr[sorted]  # swap
        sorted += 1


if __name__ == '__main__':
    #easy()
    #mid()
    bonus()