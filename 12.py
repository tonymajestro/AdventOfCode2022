# https://adventofcode.com/2022/day/12

import sys
import string
import pdb
import heapq

START, END = 44, 30
INFINITY = 10000000

def find(heightMap, toFind, toReplace):
    for i, row in enumerate(heightMap):
        for j, height in enumerate(row):
            if height == toFind:
                heightMap[i][j] = toReplace
                return i, j

def getNeighbors(x, y, heightMap):
    def isValidNeighbor(newX, newY, heightMap):
        return (0 <= newX < len(heightMap) and 
                0 <= newY < len(heightMap[0]) and
                heightMap[newX][newY] - heightMap[x][y] <= 1)

    neighbors = []
    if isValidNeighbor(x + 1, y, heightMap):
        neighbors.append((x + 1, y))
    if isValidNeighbor(x - 1, y, heightMap):
        neighbors.append((x - 1, y))
    if isValidNeighbor(x, y + 1, heightMap):
        neighbors.append((x, y + 1))
    if isValidNeighbor(x, y - 1, heightMap):
        neighbors.append((x, y - 1))

    return neighbors

def dijkstras(startX, startY, endX, endY, heightMap):
    visited = set()
    queue = []
    heapq.heappush(queue, (0, startX, startY))

    shortestPaths = [[INFINITY for j in range(len(heightMap[0]))] for i in range(len(heightMap))]
    shortestPaths[startX][startY] = 0

    while len(queue) > 0:
        shortestPath, x, y = heapq.heappop(queue)
        if x == endX and y == endY:
            return shortestPath
        elif (x, y) in visited:
            continue

        for neighborX, neighborY in getNeighbors(x, y, heightMap):
            if (neighborX, neighborY) in visited:
                continue

            currDistance = shortestPath + 1
            if currDistance < shortestPaths[neighborX][neighborY]:
                shortestPaths[neighborX][neighborY] = currDistance

            heapq.heappush(queue, (shortestPaths[neighborX][neighborY], neighborX, neighborY))

        visited.add((x, y))

    # Not found
    return INFINITY

def solve1(startX, startY, endX, endY, heightMap):
    return dijkstras(startX, startY, endX, endY, heightMap)

def solve2(startX, startY, endX, endY, heightMap):
    startingPositions = [(startX, startY)]

    for i in range(len(heightMap)):
        for j in range(len(heightMap[0])):
            if heightMap[i][j] == 0:
                startingPositions.append((i, j))

    return min(dijkstras(x, y, endX, endY, heightMap) for x, y in startingPositions)
            
if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('12.in')

    heightMap = [[string.ascii_letters.find(c) for c in line.rstrip()] for line in inputfile.readlines()]
    startX, startY = find(heightMap, START, string.ascii_lowercase.find('a'))
    endX, endY = find(heightMap, END, string.ascii_lowercase.find('z'))

    print(solve1(startX, startY, endX, endY, heightMap))
    print(solve2(startX, startY, endX, endY, heightMap))

