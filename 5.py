# https://adventofcode.com/2022/day/5

import sys

class Move(object):
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end

def solve1(crates, moves):
    for move in moves:
        for i in range(move.count):
            item = crates[move.start].pop()
            crates[move.end].append(item)

    return ''.join(stack.pop() for stack in crates)

def solve2(crates, moves):
    for move in moves:
        # Add items to be removed to a separate stack to reverse the order
        itemsToRemove = []
        for i in range(move.count):
            item = crates[move.start].pop()
            itemsToRemove.append(item)

        for i in range(len(itemsToRemove)):
            crates[move.end].append(itemsToRemove.pop())

    return ''.join(stack.pop() for stack in crates)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    crates = []
    moves = []
    with open(sys.argv[1]) as f:
        for line in f:
            if '[' in line and ']' in line:
                # Initialize crate lists
                if len(crates) == 0:
                    crates.extend([[] for _ in range((len(line) + 1) // 4)])

                for i in range((len(line) + 1) // 4):
                    item = line[(i * 4) + 1]
                    if not item.isspace():
                        crates[i].insert(0, item)
                
            elif line.startswith('move'):
                # Use 0 based indexing instead of 1 based indexing for start and end
                split = line.split()
                moves.append(Move(int(split[1]), int(split[3]) - 1, int(split[5]) - 1))

    print(solve2(crates, moves))

                



