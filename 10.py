# https://adventofcode.com/2022/day/10

import sys
from collections import deque

def solve1(commands):
    cycle = 1
    register = 1

    writing = False
    valueToWrite = 0

    signal = 0
    commandQueue = deque(commands)

    while True:
        if cycle in (20, 60, 100, 140, 180, 220):
            signal += (cycle * register)

        if writing:
            writing = False
            register += valueToWrite
        else:
            if len(commandQueue) == 0:
                break

            command = commandQueue.popleft()
            if command.startswith('addx'):
                writing = True
                valueToWrite = int(command.split()[1])

        cycle += 1

    return signal

def solve2(commands):
    # Mod calculations work better with 0 indexing
    cycle = 0
    register = 0

    writing = False
    valueToWrite = 0

    commandQueue = deque(commands)
    screen = [['.' for i in range(40)] for j in range(6)]

    while True:
        if register <= (cycle % 40) <= register + 2:
            screen[cycle // 40][cycle % 40] = '#'

        if writing:
            writing = False
            register += valueToWrite
        else:
            if len(commandQueue) == 0:
                break

            command = commandQueue.popleft()
            if command.startswith('addx'):
                writing = True
                valueToWrite = int(command.split()[1])

        cycle += 1

    for line in screen:
        print(' '.join(line))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        inputfile = open(sys.argv[1])
    else:
        inputfile = open('10.in')

    commands = [line.rstrip() for line in inputfile]

    print(solve1(commands))
    solve2(commands)
