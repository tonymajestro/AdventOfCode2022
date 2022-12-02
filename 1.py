import sys

def solve1(elves):
    calories = [sum(elf) for elf in elves]
    return max(calories)

def solve2(elves):
    calories = [sum(elf) for elf in elves]
    calories.sort()
    return sum(calories[-3:])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    elves = []
    with open(sys.argv[1]) as f:
        calories = []
        for line in f:
            if line.isspace():
                elves.append(calories)
                calories = []
            else:
                calories.append(int(line))

    # Fetch last calorie count
    elves.append(calories)

    print(solve2(elves))

