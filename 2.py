import sys

def solve1(rounds):
    scores = {
        ('A', 'X'): 4, # Tie against rock with rock
        ('A', 'Y'): 8, # Win against rock with paper
        ('A', 'Z'): 3, # Lose against rock with scissors
        ('B', 'X'): 1, # Lose against paper with rock
        ('B', 'Y'): 5, # Tie against paper with paper
        ('B', 'Z'): 9, # Win against paper with scissors
        ('C', 'X'): 7, # Win against scissors with rock
        ('C', 'Y'): 2, # Lose against scissors with paper
        ('C', 'Z'): 6, # Tie against scissors with scissors
    }

    total = 0
    for r in rounds:
        player1, player2 = r.split()
        total += scores[(player1, player2)]
    return total


def solve2(elves):
    scores = {
        ('A', 'X'): 3, # Lose against rock with scissors
        ('A', 'Y'): 4, # Tie against rock with rock
        ('A', 'Z'): 8, # Win against rock with paper
        ('B', 'X'): 1, # Lose against paper with rock
        ('B', 'Y'): 5, # Tie against paper with paper
        ('B', 'Z'): 9, # Win against paper with scissors
        ('C', 'X'): 2, # Lose against scissors with paper
        ('C', 'Y'): 6, # Tie against scissors with scissors
        ('C', 'Z'): 7, # Win against scissors with rock
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
    print(solve2(rounds))
            
        



