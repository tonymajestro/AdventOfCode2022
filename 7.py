# https://adventofcode.com/2022/day/7

import sys

class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Directory(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.directories = []
        self.files = []
        self._size = 0

    def addFile(self, filename, size):
        self.files.append(File(filename, size))

    def addDirectory(self, directoryName):
        newDirectory = Directory(self, directoryName)
        self.directories.append(newDirectory)
        return newDirectory

    def size(self):
        if self._size == 0:
            fileSize = sum(f.size for f in self.files)
            directorySize = sum(directory.size() for directory in self.directories)
            self._size = fileSize + directorySize

        return self._size

def cd(currDirectory, newDirectoryName):
    if newDirectoryName == '..':
        return currDirectory.parent
    else:
        return currDirectory.addDirectory(newDirectoryName)

def parse(commands):
    root = Directory(None, '/')
    curr = root

    for command in commands[1:]:
        split = command.split()

        # Executing cd or ls command
        if split[0] == '$':
            if split[1] == 'cd':
                curr = cd(curr, split[2])
        # Listing files/subdirectories from ls
        else:
            # Add files to the current directory
            # We'll create sub-directories when we 'cd' into them
            if split[0] != 'dir':
                curr.addFile(split[1], int(split[0]))

    return root

def solve1(directory):
    total = sum(solve1(sub) for sub in directory.directories)

    if directory.size() <= 100000:
        total += directory.size()

    return total

def solve2(directory, toFree):
    if directory.size() < toFree:
        return 70000000  # Some large number bound by max disk space

    smallestToFree = directory.size()

    for sub in directory.directories:
        smallestToFree = min(smallestToFree, solve2(sub, toFree))

    return smallestToFree

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    commands = [line.rstrip() for line in open(sys.argv[1]).readlines()]

    root = parse(commands)
    unused = 70000000 - root.size()
    toFree = 30000000 - unused

    print(solve1(root))
    print(solve2(root, toFree))
