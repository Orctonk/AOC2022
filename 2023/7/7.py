f = open("2023/7/input.txt")

pairs = []

for l in f.readlines():
  raws = l.strip().split(" ")

  pairs.append((raws[0],int(raws[1])))


def HandValue(hand: str):
  freqs = {}
  for c in hand:
    if not c in freqs:
      freqs[c] = 0

    freqs[c] = freqs[c] + 1

  score = 0
  freqlist = [(k,freqs[k]) for k in freqs]
  freqs = sorted(freqlist, key=lambda x: x[1],reverse=True)
  if freqs[0][1] == 5:
    score += 6000000
  elif freqs[0][1] == 4:
    score += 5000000
  elif freqs[0][1] == 3 and freqs[1][1] == 2:
    score += 4000000
  elif freqs[0][1] == 3:
    score += 3000000
  elif freqs[0][1] == 2 and freqs[1][1] == 2:
    score += 2000000
  elif freqs[0][1] == 2:
    score += 1000000

  cvals = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

  for i,c in enumerate(hand):
    if c in cvals:
      score += cvals[c] * 16 ** (4 - i)
    else:
      score += int(c) * 16 ** (4 - i)
  return score

pairs.sort(key=lambda x: HandValue(x[0]))

totScore = 0

for i, p in enumerate(pairs):
  totScore += (i+1) * p[1]

print(totScore)
print("Part 2")

def HandValueP2(hand: str):
  freqs = {}
  for c in hand:
    if not c in freqs:
      freqs[c] = 0

    freqs[c] = freqs[c] + 1

  score = 0
  js = freqs.pop("J",0)

  if len(freqs) == 0:
    freqs["J"] = 0

  freqlist = [(k,freqs[k]) for k in freqs]
  freqs = sorted(freqlist, key=lambda x: x[1],reverse=True)

  freqs[0] = (freqs[0][0],freqs[0][1] + js)
  if freqs[0][1] == 5:
    score += 6000000
  elif freqs[0][1] == 4:
    score += 5000000
  elif freqs[0][1] == 3 and freqs[1][1] == 2:
    score += 4000000
  elif freqs[0][1] == 3:
    score += 3000000
  elif freqs[0][1] == 2 and freqs[1][1] == 2:
    score += 2000000
  elif freqs[0][1] == 2:
    score += 1000000

  cvals = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}

  for i,c in enumerate(hand):
    if c in cvals:
      score += cvals[c] * 16 ** (4 - i)
    else:
      score += int(c) * 16 ** (4 - i)
  return score

pairs.sort(key=lambda x: HandValueP2(x[0]))

totScore = 0

for i, p in enumerate(pairs):
  totScore += (i+1) * p[1]

print(totScore)