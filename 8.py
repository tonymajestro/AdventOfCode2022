# https://adventofcode.com/2022/day/8

import sys

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

def isVisibileInDirection(trees, x, y, direction):
    xOffset, yOffset = direction
    i, j = x + xOffset, y + yOffset

    while i >= 0 and i < len(trees) and j >= 0 and j < len(trees):
        if trees[i][j] >= trees[x][y]:
            return False

        i += xOffset
        j += yOffset

    return True

def numTreesVisible(trees, x, y, direction):
    xOffset, yOffset = direction
    i, j = x + xOffset, y + yOffset
    total = 0

    while i >= 0 and i < len(trees) and j >= 0 and j < len(trees):
        total += 1
        if trees[i][j] >= trees[x][y]:
            break
        i += xOffset
        j += yOffset

    return total

def solve1(trees):
    total = 0
    for i in range(len(trees)):
        for j in range(len(trees)):
            if (isVisibileInDirection(trees, i, j, LEFT) or
                isVisibileInDirection(trees, i, j, RIGHT) or
                isVisibileInDirection(trees, i, j, UP) or
                isVisibileInDirection(trees, i, j, DOWN)):
                total += 1

    return total

def solve2(trees):
    maxScenicScore = -1
    for i in range(len(trees)):
        for j in range(len(trees)):
            scenicScore = (numTreesVisible(trees, i, j, LEFT) * 
                           numTreesVisible(trees, i, j, RIGHT) * 
                           numTreesVisible(trees, i, j, UP) * 
                           numTreesVisible(trees, i, j, DOWN))
            maxScenicScore = max(maxScenicScore, scenicScore)

    return maxScenicScore


if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('8.in')

    trees = [[int(tree) for tree in line.rstrip()] for line in inputfile.readlines()]
    print(solve1(trees))
    print(solve2(trees))

