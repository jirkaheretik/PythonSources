import math 

report = False

def readFile(filename):
    inputValues = dict()
    f = open(filename, "r")
    if f.mode == "r":
        for x in f:
            #inputValues.append(x.strip())
            name, expr = x.strip().split(": ")
            inputValues[name] = expr
    return inputValues
    
def getValue(monkeys, monkey):
    global report
    expr = monkeys[monkey]
    try:
        if monkey == "humn":
            print(f"Humn monkey value: {expr}")
            # report = True
        if isinstance(expr, int):
            return expr
        elif expr.isdigit():
            monkeys[monkey] = int(expr)
            return int(expr)
        else:
            left, oper, right = expr.split(" ")
            result = doOper(oper, getValue(monkeys, left), getValue(monkeys, right))
            if report:
                print(f"Monkey {monkey}: {left} {oper} {right} == {result}")
            monkeys[monkey] = result
            return result
    except Exception as ex:
        print(f"Err ({ex}) {expr} of type {type(expr)}")
        left, oper, right = expr.split(" ")
        result = doOper(oper, getValue(monkeys, left), getValue(monkeys, right))
        if report:
            print(f"Monkey {monkey}: {left} {oper} {right} == {result}")
        monkeys[monkey] = result
        return result

def doOper(oper, val1, val2):
    if "+" == oper:
        return val1 + val2
    elif "-" == oper:
        return val1 - val2
    elif "*" == oper:
        return val1 * val2
    elif "/" == oper:
        return val1 // val2
    else:
        print(f"Unknown operation {oper} on {val1} and {val2}")
        return 0 
    
def processValues1(vstup):
    score = 0
    return getValue(vstup, "root")
    
def processValues2(vstup):
    score = 0
    vstup["humn"] = 3560293715732
    left = getValue(vstup, "lzfc")  # tady nekde je humn
    print(f"Left:  {left}")
    right = getValue(vstup, "qrgn")
    print(f"Right: {right}")
    return left - right

if __name__ == "__main__":
    #myValues = readFile("d21.txt")
    #result1 = processValues1(myValues)
    myValues = readFile("d21.txt")
    result2 = processValues2(myValues)
    #print("Root monkey: {}".format(result1))
    print("Human/Root interaction: {}".format(result2))

# Failed answers P1: 
# 
