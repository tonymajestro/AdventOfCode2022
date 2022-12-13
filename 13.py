# https://adventofcode.com/2022/day/13

import sys
import json
from functools import cmp_to_key

def checkOrder(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left - right

    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip(left, right):
            result = checkOrder(l, r)
            if result != 0:
                return result
            
        # Ran out of items, compare the lengths of the arrays
        return checkOrder(len(left), len(right))

    else:
        if isinstance(left, int):
            return checkOrder([left], right) 
        else: 
            return checkOrder(left, [right])

def solve1(pairs):
    total = 0
    for i, pair in enumerate(pairs):
        if checkOrder(*pair) <= 0:
            total += (i + 1)
    
    return total

def solve2(pairs):
    packets = []
    for left, right in pairs:
        packets.append(left)
        packets.append(right)

    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=cmp_to_key(checkOrder))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('13.in')

    pairs = []
    while True:
        left = inputfile.readline().rstrip()
        right = inputfile.readline().rstrip()
        if not left or not right:
            break

        pairs.append((json.loads(left), json.loads(right)))
        inputfile.readline()

    print(solve1(pairs))
    print(solve2(pairs))
        



