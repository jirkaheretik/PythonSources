best = 0
bestCal = 0

for sugar in range(1, 100):
    for frosting in range(1, 100):
        for peanut in range(1, 100):
            sprinkles = 100 - sugar - frosting - peanut
            if sprinkles < 0:
                continue
            if 3 * peanut - sprinkles - frosting < 1:
                continue
            if 5 * sprinkles - peanut - sugar < 1:
                continue
            score = (5 * sprinkles - peanut - sugar) * (3 * peanut - sprinkles - frosting) * 8 * frosting * sugar
            calories = 8 * sugar + 6 * frosting + peanut + 5 * sprinkles
            if score > best:
                best = score
            if calories == 500 and score > bestCal:
                bestCal = score 
print(f"Max recept: {best}")
print(f"Max 500cal recept: {bestCal}")