# https://adventofcode.com/2022/day/11

import sys
from collections import deque
from functools import partial
import math
import pdb

class Monkey(object):
    def __init__(self, items, operation, worryTest, monkeyTrue, monkeyFalse):
        self.items = deque(items)
        self.operation = operation
        self.worryTest = worryTest
        self.monkeyTrue = monkeyTrue
        self.monkeyFalse = monkeyFalse
        self.inspected = 0

    def throwItems(self, monkeys, worryDecreaseLevel):
        divideBy = math.prod(monkey.worryTest for monkey in monkeys)
        while len(self.items) > 0:
            item = self.items.popleft()
            self.throw(item, monkeys, worryDecreaseLevel, divideBy)
            self.inspected += 1

    def throw(self, item, monkeys, worryDecreaseLevel, divideBy):
        worry = (self.operation(item) // worryDecreaseLevel) % divideBy
        if worry % self.worryTest == 0:
            monkeys[self.monkeyTrue].items.append(worry)
        else:
            monkeys[self.monkeyFalse].items.append(worry)

def parseItems(line):
    itemStr = line[len('Starting items: ') :].split(',')
    return [int(item.rstrip()) for item in itemStr]

def parseWorryOperation(line):
    def computeWorry(a, b, operation, value):
        op1 = value if a == 'old' else int(a)
        op2 = value if b == 'old' else int(b)

        if operation == '+':
            return op1 + op2
        elif operation == '-':
            return op1 - op2
        else:
            return op1 * op2

    a, operation, b = line.strip()[len('Operation: new = ') :].split()
    return partial(computeWorry, a, b, operation)

def parseMonkeys(inputfile):
    monkeys = []
    while True:
        if len(inputfile.readline()) == 0:
            break

        items = parseItems(inputfile.readline().strip())
        worryLine = inputfile.readline().strip()
        worryOperation = parseWorryOperation(worryLine)
        worryTest = int(inputfile.readline().strip().split()[-1])
        monkeyTrue = int(inputfile.readline().strip().split()[-1])
        monkeyFalse = int(inputfile.readline().strip().split()[-1])

        monkeys.append(Monkey(items, worryOperation, worryTest, monkeyTrue, monkeyFalse))
        inputfile.readline()

    return monkeys


def solve1(monkeys):
    worryDecreaseLevel = 3
    for i in range(20):
        for monkey in monkeys:
            monkey.throwItems(monkeys, worryDecreaseLevel)

    monkeys.sort(key=lambda monkey: monkey.inspected, reverse=True)
    return monkeys[0].inspected * monkeys[1].inspected

def solve2(monkeys):
    worryDecreaseLevel = 1
    for i in range(10000):
        for monkey in monkeys:
            monkey.throwItems(monkeys, worryDecreaseLevel)

    monkeys.sort(key=lambda monkey: monkey.inspected, reverse=True)
    return monkeys[0].inspected * monkeys[1].inspected


if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('11.in')

    monkeys = parseMonkeys(inputfile)
    print(solve2(monkeys))

