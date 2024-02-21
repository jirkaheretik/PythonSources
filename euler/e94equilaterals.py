import datetime
import math
import sys

def main():
    sum = 0

    for n in range(3, 333_333_334, 2):  # try with odds only to get integer base and half-base
        #if ((n - 1) % 10000000) == 0:
        #    print(".", end = "") # dot every 10M numbers processed
        if isIntegral(n, n - 1):
            sum += 3 * n - 1
            print(f"{n}, {n}, {n - 1}")
        if isIntegral(n, n + 1):
            sum += 3 * n + 1
            print(f"{n}, {n}, {n + 1}")

    print(f"\nSum of perimeters of almost equilateral triangles is {sum}")

def isIntegral(side, base):
    half = base // 2
    height = math.sqrt(side * side - half * half)
    hght = int(height)
    if height != hght:
        return False
    return side * side - half * half - hght * hght == 0
    #if side * side - half * half - hght * hght != 0:
    #    print(f"Possible loss of precision, not counting {side}")
    #    return False
    #return True


def test():
    print(isIntegral(5, 6))

if __name__ == '__main__':
    sys.set_int_max_str_digits(650)   # back to normal value
    print(datetime.datetime.now())
    main()
    # test()
    print(datetime.datetime.now())

# Wrong answers:
# Sum of perimeters of all 508898797 almost equilateral triangles is 312530630458602039
# v2: Sum of perimeters of all 20 almost equilateral triangles is 4489548014