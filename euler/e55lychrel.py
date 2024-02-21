def main():
    lychrelCount = 0
    limit = 10000
    for number in range(limit):
        dummy = number
        isPal = False
        for i in range(50):
            dummy = dummy + int(str(dummy)[::-1])
            # print(f"{number} .. {dummy}")
            if isPalindrome(str(dummy)):
                isPal = True
                break
        if not isPal:
            print(f"Number {number} is Lychrel Number")
            lychrelCount += 1
    print(f"There are {lychrelCount} Lychrel numbers below {limit}")


def isPalindrome(s):
    """by GeeksForGeeks"""
    return s == s[::-1]

if __name__ == '__main__':
    main()