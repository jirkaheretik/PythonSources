"""
 public static final int[] INPUT = {8435, 234, 928434, 14, 0, 7, 92446, 8992692};

    public static void main(String[] args) {
        // dbg:
        System.out.println("Example 6 steps: " + (doStep(125, 6) + doStep(17, 6)));
        System.out.println("Example 25 steps: " + (doStep(125, 25) + doStep(17, 25)));
        // real data:
        long sum = 0;
        for (int num: INPUT)
            sum += doStep(num, 25);
        System.out.println("Part 1 number of stones after 25 steps: " + sum);
        // 182080 - too low
    }

    public static int doStep(long number, int remains) {
        if (remains == 0) return 1;
        if (number == 0) return doStep(1, remains - 1);
        if (number == 1) return doStep(2024, remains - 1);
        int digits = (int)Math.ceil(Math.log10(number));
        if (digits % 2 == 0) {
            long tens = (int)Math.pow(10, digits / 2);
            return doStep(number / tens, remains - 1) + doStep(number % tens, remains - 1);
        } else return doStep(number * 2024, remains - 1);

"""
import math


def doStep(number, remains):
    if remains == 0:
        # print(f"{number} ", end="")
        return 1
    if number == 0:
        return doStep(1, remains - 1)
    if number == 1:
        return doStep(2024, remains - 1)
    # digits = int(math.ceil(math.log10(number)))
    strnum = str(number)
    if len(strnum) % 2 == 0:
        half = len(strnum) // 2
        return doStep(int(strnum[:half]), remains - 1) + doStep(int(strnum[half:]), remains - 1)
    else:
        return doStep(number * 2024, remains - 1)
    """
    if digits == 0:
        print(f"Huh, number {number}, remains {remains} and counted digits {digits}")
    if digits % 2 == 0:
        tens = math.pow(10, digits // 2)
        return doStep(number // tens, remains - 1) + doStep(number % tens, remains - 1)
    """

numbers = [8435, 234, 928434, 14, 0, 7, 92446, 8992692]
testnums = [125, 17, 0, 7, 14, 2024, 8435, 928434, 8992692]
example = [125, 17]
steps = 75

sum = 0
#for num in example:
#    sum += doStep(num, steps)
#print(f"Example number: {sum}")

sum = 0
for num in numbers:
    res = doStep(num, steps)
    print(f"{num} - stones: {res}")
    sum += res
print(f"Real output number: {sum}")

# for num in testnums:
#    print(f"{num} - stones: {doStep(num, 75)}")
