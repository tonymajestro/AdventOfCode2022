# https://adventofcode.com/2022/day/14

import sys

INFINITY = 1000000
OUT_OF_BOUNDS = -1000000
VALID = 1

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

    # Initialize grid
    numColumns = maxX - minX
    grid = [['.' for j in range(maxY + 1)] for i in range(numColumns + 1)]

    # Fill in all rock points
    for rockLine in rocks:
        for i in range(len(rockLine) - 1):
            startPoint, stopPoint = rockLine[i], rockLine[i+1]
            fill(grid, startPoint, stopPoint)

    sandStart = Point(500 - minX, 0)
    return grid, sandStart

def extendGridForPart2(grid, sandStart):
    # Compute location of infinite floor
    maxRockY = 0
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == '#':
                maxRockY = max(maxRockY, j)

    # Extend grid in Y direction if needed to handle new infinite floor
    floorY = maxRockY + 2
    if floorY >= len(grid[0]):
        for column in grid:
            column.extend(['.', '.'])

    # Extend grid in both x directions to enable an infinite floor
    extendedLength = 200
    extendedLeft = [['.' for j in range(len(grid[0]))] for i in range(extendedLength)]
    extendedRight = [['.' for j in range(len(grid[0]))] for i in range(extendedLength)]
    grid = extendedLeft + grid + extendedRight

    # Create infinite floor
    for i in range(len(grid)):
        grid[i][floorY] = '#'

    newSandStart = Point(sandStart.x + extendedLength, sandStart.y)
    return grid, newSandStart

def checkSand(grid, sandPoint):
    if sandPoint.x < 0 or sandPoint.x >= len(grid) or sandPoint.y >= len(grid[0]):
        return True

    return grid[sandPoint.x][sandPoint.y] not in ('#', 'o')

def simulate(grid, sandPoint):
    down = Point(sandPoint.x, sandPoint.y + 1)
    downLeft = Point(sandPoint.x - 1, sandPoint.y + 1)
    downRight = Point(sandPoint.x + 1, sandPoint.y + 1)

    if checkSand(grid, down):
        return down
    elif checkSand(grid, downLeft):
        return downLeft
    elif checkSand(grid, downRight):
        return downRight
    else:
        return sandPoint

def solve1(grid, sandStart):
    currentSandPoint = Point(sandStart.x, sandStart.y)
    sandCount = 0

    while True:
        newSandPoint = simulate(grid, currentSandPoint)
        if newSandPoint.x < 0 or newSandPoint.x >= len(grid) or newSandPoint.y >= len(grid[0]):
            grid[currentSandPoint.x][currentSandPoint.y] = 'o'
            sandCount += 1
            break
        elif newSandPoint == currentSandPoint:
            grid[currentSandPoint.x][currentSandPoint.y] = 'o'
            currentSandPoint = Point(sandStart.x, sandStart.y)
            sandCount += 1
        else:
            currentSandPoint = newSandPoint

    return sandCount

def solve2(grid, sandStart):
    newGrid, newSandStart = extendGridForPart2(grid, sandStart)
    currentSandPoint = newSandStart
    sandCount = 0
    
    while True:
        newSandPoint = simulate(newGrid, currentSandPoint) 
        if newSandPoint == newSandStart:
            break
        elif newSandPoint == currentSandPoint:
            newGrid[currentSandPoint.x][currentSandPoint.y] = 'o'
            currentSandPoint = Point(newSandStart.x, newSandStart.y)
            sandCount += 1
        else:
            currentSandPoint = newSandPoint

    return sandCount
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('14.in')

    lines = [line.rstrip() for line in inputfile.readlines()]
    grid1, sandStart = parseGrid(lines)
    grid2 = [[c for c in column] for column in grid1]

    print(solve1(grid1, sandStart))
    print(solve2(grid2, sandStart))


