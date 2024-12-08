def romanToInt(s: str) -> int:
    _LETTERS = "MDCLXVI"
    _VALUES = [1000, 500, 100, 50, 10, 5, 1]

    result = 0
    value = _VALUES[_LETTERS.index(s[0])]
    if len(s) == 1: return value
    nextValue = 0
    for index in range(1, len(s)):
        nextValue = _VALUES[_LETTERS.index(s[index])]
        result += value * (-1 if nextValue > value else 1)
        value = nextValue
    return result + nextValue

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))