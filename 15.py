# https://adventofcode.com/2022/day/15

import sys
from collections import namedtuple
import pdb

ROW_TO_SEARCH = 2000000
BOUNDS = 4000000
#ROW_TO_SEARCH = 10
#BOUNDS = 20

def manhattanDistance(sensor, beacon):
    return abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

def findNoBeacons(sensorsAndBeacons, rowToSearch):
    noBeacons = set()
    for sensor, closestBeacon in sensorsAndBeacons:
        distance = manhattanDistance(sensor, closestBeacon)
        if sensor.y - distance <= rowToSearch <= sensor.y + distance:
            startX = sensor.x - (distance - abs(sensor.y - rowToSearch))
            stopX = sensor.x + (distance - abs(sensor.y - rowToSearch))
            for i in range(startX, stopX + 1):
                if closestBeacon.x != i or closestBeacon.y != rowToSearch:
                    noBeacons.add(i)

    return noBeacons

def findNoBeaconsWithBounds(sensorsAndBeacons, rowToSearch, bounds):
    noBeacons = set()
    for sensor, closestBeacon in sensorsAndBeacons:
        distance = manhattanDistance(sensor, closestBeacon)
        if sensor.y - distance <= rowToSearch <= sensor.y + distance:
            startX = min(0, sensor.x - (distance - abs(sensor.y - rowToSearch)))
            stopX = max(bounds + 1, sensor.x + (distance - abs(sensor.y - rowToSearch)))
            for i in range(startX, stopX + 1):
                noBeacons.add(i)

    return noBeacons

def solve1(sensorsAndBeacons, rowToSearch):
    return findNoBeacons(sensorsAndBeacons, rowToSearch)

def solve2(sensorsAndBeacons):
    #pdb.set_trace()
    beacons = [beacon for sensor, beacon in sensorsAndBeacons]
    for row in range(BOUNDS + 1):
        noBeacons = findNoBeaconsWithBounds(sensorsAndBeacons, row, BOUNDS)
        noBeacons.update(beacon.x for beacon in beacons if beacon.y == row)

        print(row)
        if len(noBeacons) == BOUNDS + 1:
            continue

        for i in range(BOUNDS + 1):
            if i not in noBeacons:
                #pdb.set_trace()
                return (i * 4000000) + row
        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('15.in')

    Point = namedtuple("Point", ["x", "y"])

    sensorsAndBeacons = []
    for line in inputfile:
        split = line.strip().split()
        sensorX, sensorY, beaconX, beaconY = int(split[2][2:-1]), int(split[3][2:-1]), int(split[8][2:-1]), int(split[9][2:])
        sensorsAndBeacons.append((Point(sensorX, sensorY), Point(beaconX, beaconY)))
    
    print(len(solve1(sensorsAndBeacons, ROW_TO_SEARCH)))
    print(solve2(sensorsAndBeacons))

