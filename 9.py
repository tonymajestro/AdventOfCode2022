# https://adventofcode.com/2022/day/9

import sys

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, xOffset, yOffset):
        self.x += xOffset
        self.y += yOffset

directions = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1), 
    'D': (0, -1), 
}

def normalize(offset):
    if offset > 0:
        return 1
    elif offset < 0:
        return -1
    else:
        return 0

def moveHead(head, direction):
    xOffset, yOffset = directions[direction]
    head.move(xOffset, yOffset)

def moveTail(head, tail):
    xOffset = head.x - tail.x
    yOffset = head.y - tail.y

    if abs(xOffset) <= 1 and abs(yOffset) <= 1:
        return

    normalizedXOffset = normalize(xOffset)
    normalizedYOffset = normalize(yOffset)
    tail.move(normalizedXOffset, normalizedYOffset)

def solve(moves, knots):
    head, tail = knots[0], knots[-1]

    uniquePositions = set()
    uniquePositions.add((tail.x, tail.y))

    for move in moves:
        direction, count = move[0], int(move[1])
        for _ in range(count):
            moveHead(head, direction)

            for j in range(1, len(knots)):
                curr, prev = knots[j], knots[j - 1]
                moveTail(prev, curr)

            uniquePositions.add((tail.x, tail.y))

    return len(uniquePositions)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('9.in')

    moves = [line.split() for line in inputfile.readlines()]
    knots1 = [Point(), Point()]
    print(solve(moves, knots1))

    knots2 = [Point() for i in range(10)]
    print(solve(moves, knots2))
