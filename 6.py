# https://adventofcode.com/2022/day/6

import sys

def solve(transmission, markerLength):
    for i in range(len(transmission) - markerLength):
        marker = transmission[i:i+markerLength]
        if len(set(marker)) == markerLength:
            return i + markerLength

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    transmission = open(sys.argv[1]).read().rstrip()
    print(solve(transmission, 4))
    print(solve(transmission, 14))
