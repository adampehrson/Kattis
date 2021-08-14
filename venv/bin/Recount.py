import sys

candidates = dict()
total = 0

while True:
    name = sys.stdin.readline().strip()
    if name == "***":
        break

    if name in candidates.keys():
        candidates[name] += 1
    else:
        candidates.update({name: 1})
    total += 1


runoff = False
votes = 0
winner = ""

for x in candidates:
    if candidates[x] == votes:
        runoff = True
    elif candidates[x] > votes:
        votes = candidates[x]
        winner = x
        runoff = False

if runoff:
    print("Runoff!")
else:
    print(winner)