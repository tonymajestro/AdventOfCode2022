import sys

ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
TIE = 3
WIN = 6

def solve1(rounds):
    scores = {
        ('A', 'X'): TIE + ROCK,
        ('A', 'Y'): WIN + PAPER,
        ('A', 'Z'): LOSS + SCISSORS,
        ('B', 'X'): LOSS + ROCK,
        ('B', 'Y'): TIE + PAPER,
        ('B', 'Z'): WIN + SCISSORS,
        ('C', 'X'): WIN + ROCK,
        ('C', 'Y'): LOSS + PAPER,
        ('C', 'Z'): TIE + SCISSORS
    }

    total = 0
    for r in rounds:
        player1, player2 = r.split()
        total += scores[(player1, player2)]
    return total


def solve2(elves):
    scores = {
        ('A', 'X'): LOSS + SCISSORS,
        ('A', 'Y'): TIE + ROCK,
        ('A', 'Z'): WIN + PAPER,
        ('B', 'X'): LOSS + ROCK,
        ('B', 'Y'): TIE + PAPER,
        ('B', 'Z'): WIN + SCISSORS,
        ('C', 'X'): LOSS + PAPER,
        ('C', 'Y'): TIE + SCISSORS,
        ('C', 'Z'): WIN + ROCK
    }

    total = 0
    for r in rounds:
        player1, end = r.split()
        total += scores[(player1, end)]
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Input file required", file=sys.stderr)
        exit(1)

    rounds = [line.rstrip() for line in open(sys.argv[1]).readlines()]
    print(solve1(rounds))
