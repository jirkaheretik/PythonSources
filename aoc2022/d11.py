from pprint import pprint
# from numpy import sign
import math

"""INPUT:

Monkey 0:
  Starting items: 57, 58
  Operation: new = old * 19
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 66, 52, 59, 79, 94, 73
  Operation: new = old + 1
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 6

Monkey 2:
  Starting items: 80
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 82, 81, 68, 66, 71, 83, 75, 97
  Operation: new = old + 5
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 55, 52, 67, 70, 69, 94, 90
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 69, 85, 89, 91
  Operation: new = old + 7
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 7

Monkey 6:
  Starting items: 75, 53, 73, 52, 75
  Operation: new = old * 7
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 7:
  Starting items: 94, 60, 79
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 1
    If false: throw to monkey 6"""

class Monkey:
    TOTAL = 9699690  # Product of all the monkeys dividers
    #TOTAL = 96577   # Product of all the monkeys dividers (TEST RUN)
    def __init__(self, idx, start, update, test):
        self._idx = idx  # "name" of the monkey, its index
        self._items = start
        self._update = update
        self._test = test
        self._inspected = 0
        
    def newItem(self, item):
        self._items.append(item)
        
    def setNeighbours(self, tValue, fValue):
        self._true = tValue
        self._false = fValue
        
    def test(self, val):
        return val % self._test == 0
        
    def turn(self):
        for item in self._items:
            self._inspected += 1
            #item = self._update(item) // 3  # PROBLEM 1 ONLY
            item = self._update(item) % Monkey.TOTAL
            if self.test(item):
                self._true.newItem(item)
            else:
                self._false.newItem(item)
        self._items = []
    
    def getInspected(self):
        return self._inspected
    
    def __str__(self):
        return f"Monkey {self._idx}: {self._items}"        
            

def sg(x):
    return (x > 0) - (x < 0)

def readFile(filename):
    inputValues = []
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            inputValues.append(x.strip())
    return inputValues
    

def processValues1(monkeys):
    score = 0
    #for round in range(20):  # PROBLEM1 
    for round in range(10000):
        for monkey in monkeys:
            monkey.turn()
        print(f"After round {round}, monkeys are holding items with these worry levels:")
        for monkey in monkeys:
            print(monkey)
    # get the activity:
    activity = []
    for monkey in monkeys:
        activity.append(monkey.getInspected()) 
    activity.sort(reverse = True)  
    print(f"Activity levels after full run: {activity}")          
    return activity[0] * activity[1]
    
def processValues2(load):
    score = 0
    return score

if __name__ == "__main__":
    #myValues = readFile("d10.txt")
    myValues = []
    #"""
    myValues.append(Monkey(0, [57, 58], lambda a: a*19, 7))
    myValues.append(Monkey(1, [66, 52, 59, 79, 94, 73], lambda a: a+1, 19))
    myValues.append(Monkey(2, [80], lambda a: a+6, 5))
    myValues.append(Monkey(3, [82, 81, 68, 66, 71, 83, 75, 97], lambda a: a+5, 11))
    myValues.append(Monkey(4, [55, 52, 67, 70, 69, 94, 90], lambda a: a*a, 17))
    myValues.append(Monkey(5, [69, 85, 89, 91], lambda a: a+7, 13))
    myValues.append(Monkey(6, [75, 53, 73, 52, 75], lambda a: a*7, 2))
    myValues.append(Monkey(7, [94, 60, 79], lambda a: a+2, 3))
    myValues[0].setNeighbours(myValues[2], myValues[3])
    myValues[1].setNeighbours(myValues[4], myValues[6])
    myValues[2].setNeighbours(myValues[7], myValues[5])
    myValues[3].setNeighbours(myValues[5], myValues[2])
    myValues[4].setNeighbours(myValues[0], myValues[3])
    myValues[5].setNeighbours(myValues[1], myValues[7])
    myValues[6].setNeighbours(myValues[0], myValues[4])
    myValues[7].setNeighbours(myValues[1], myValues[6])
    """
    # test run:
    myValues.append(Monkey(0, [79, 98], lambda a: a*19, 23))
    myValues.append(Monkey(1, [54, 65, 75, 74], lambda a: a+6, 19))
    myValues.append(Monkey(2, [79, 60, 97], lambda a: a*a, 13))
    myValues.append(Monkey(3, [74], lambda a: a+3, 17))
    myValues[0].setNeighbours(myValues[2], myValues[3])
    myValues[1].setNeighbours(myValues[2], myValues[0])
    myValues[2].setNeighbours(myValues[1], myValues[3])
    myValues[3].setNeighbours(myValues[0], myValues[1])
    """
    result1 = processValues1(myValues)
    result2 = processValues2(myValues)
    print("Monkey business: {}".format(result1))
    #print("Long tail positions {}".format(result2))

# 1st try: 238*235=55930, too high 