# https://adventofcode.com/2022/day/14

import sys

INFINITY = 1000000

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'

def debug(grid):
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            print(grid[i][j], end='')
        print()

def fill(grid, startPoint, stopPoint):
    if startPoint.x == stopPoint.x:
        startY = min(startPoint.y, stopPoint.y)
        stopY = max(startPoint.y, stopPoint.y)
        for j in range(startY, stopY + 1):
            grid[startPoint.x][j] = '#'
    else:
        startX = min(startPoint.x, stopPoint.x)
        stopX = max(startPoint.x, stopPoint.x)
        for i in range(startX, stopX + 1):
            grid[i][startPoint.y] = '#'

def parseGrid(lines):
    # Set up lines of rocks
    rocks = []
    maxX, maxY = 0, 0
    minX = INFINITY
    for line in lines:
        points = line.rstrip().split(' -> ')
        rockLine = []
        for point in points:
            x, y = map(int, point.split(','))
            rockLine.append(Point(x, y))
            maxX = max(maxX, x)
            maxY = max(maxY, y)
            minX = min(minX, x)

        rocks.append(rockLine)

    # Normalize rock points to begin at 0,0 etc
    for line in rocks:
        for point in line:
            point.x -= minX
            print(point)

    # Initialize grid
    numColumns = maxX - minX
    grid = [['.' for j in range(numColumns + 1)] for i in range(maxY + 1)]
    print(len(grid))
    print(len(grid[0]))

    # Fill in all rock points
    for rockLine in rocks:
        for i in range(len(rockLine) - 1):
            startPoint, stopPoint = rockLine[i], rockLine[i+1]
            fill(grid, startPoint, stopPoint)

    sandStart = Point(500 - minX, 0)
    return grid, sandStart

def checkSand(grid, sandPoint):
    return (0 <= sandPoint.x < len(grid) and
            0 <= sandPoint.y < len(grid[0]) and
            grid[sandPoint.x][sandPoint.y] != '#')

def simulate(grid, sandPoint):
    down = Point(sandPoint.x, sandPoint.y + 1)
    downLeft = Point(sandPoint.x - 1, sandPoint.y + 1)
    downRight = Point(sandPoint.x - 1, sandPoint.y + 1)

    if checkSand(grid, down):
        return down
    elif checkSand(grid, downLeft):
        return downLeft
    elif checkSand(grid, downRight):
        return downRight
    else:
        return sandPoint

def solve1(grid, sandStart):


if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('14.in')

    lines = [line.rstrip() for line in inputfile.readlines()]
    grid, sandStart = parseGrid(lines)
    debug(grid)


