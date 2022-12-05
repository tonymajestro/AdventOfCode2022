# https://adventofcode.com/2022/day/4

import sys

def parse_assignments(assignment):
    elf1, elf2 = assignment.split(',')

    low1, high1 = map(int, elf1.split('-'))
    low2, high2 = map(int, elf2.split('-'))

    return (low1, high1, low2, high2)

def solve1(assignments):
    total = 0
    for assignment in assignments:
        low1, high1, low2, high2 = parse_assignments(assignment)
        if (low1 <= low2 and high1 >= high2) or (low2 <= low1 and high2 >= high1):
            total += 1

    return total


def solve2(assignments):
    total = 0
    for assignment in assignments:
        low1, high1, low2, high2 = parse_assignments(assignment)
        if (low1 <= low2 <= high1 or
            low1 <= high2 <= high1 or
            low2 <= low1 <= high2 or
            low2 <= high1 <= high2):
            total += 1

    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    assignments = [line.rstrip() for line in open(sys.argv[1]).readlines()]
    print(solve1(assignments))
    print(solve2(assignments))
