ROCK = 0
PAPER = 1
SCISSORS = 2
CHOICES = 3

LOSE = 0
DRAW = 1
WIN = 2


def calcRoundScore(their, ours):
    score = ours + 1
    if ours == (their + 1) % CHOICES:
        score += 6
    elif ours == their:
        score += 3

    return score


f = open("2/input.txt")

total = 0
rounds = 0
for l in f:
    their = ord(l[0]) - ord('A')
    strat = ord(l[2]) - ord('X')
    ours = -1
    if strat == DRAW:
        ours = their
    elif strat == LOSE:
        ours = (their + 2) % CHOICES
    elif strat == WIN:
        ours = (their + 1) % CHOICES
    total += calcRoundScore(their, ours)
    rounds += 1

print(rounds)
print(total)
