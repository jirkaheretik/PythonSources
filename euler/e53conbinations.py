
def main():
    faktorialy = list()
    faktorialy.append(1)
    faktorialy.append(1)
    for i in range(2, 101):
        faktorialy.append(i * faktorialy[i - 1])
    pocetNad1M = 0
    for n in range(23, 101):
        for r in range(2, n):
            if faktorialy[n] / faktorialy[r] / faktorialy[n - r] > 1000000:
                pocetNad1M += 1
    print(f"Kombinacnich cisel nad 1M je {pocetNad1M}")


if __name__ == '__main__':
    main()