# https://adventofcode.com/2022/day/3

import string
import sys

def priority(c):
    # string.ascii_letters -> 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # position in string.ascii_letters + 1 represents the priority for the item
    return string.ascii_letters.find(c) + 1

def solve1(rucksacks):
    total = 0
    for rucksack in rucksacks:
        compartment1 = set(rucksack[:len(rucksack) // 2])
        compartment2 = set(rucksack[len(rucksack) // 2:])
        intersection = compartment1.intersection(compartment2)

        total += sum(priority(c) for c in intersection)

    return total

def solve2(rucksacks):
    total = 0
    for i in range(len(rucksacks) // 3):
        group = rucksacks[i*3 : i*3 + 3]
        elf1, elf2, elf3 = [set(rucksack) for rucksack in group]
        intersection = elf1.intersection(elf2).intersection(elf3)
        total += sum(priority(c) for c in intersection)

    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    rucksacks = [line.rstrip() for line in open(sys.argv[1]).readlines()]
    print(solve2(rucksacks))
