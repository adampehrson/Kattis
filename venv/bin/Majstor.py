def svenscore(a,b):
    if a == b:
        return 1
    if a == "R" and b == "S":
        return 2
    if a == "S" and b == "P":
        return 2
    if a == "P" and b == "R":
        return 2
    else:
        return 0

rounds = int(input())

sven = input()

amount = int(input())
friends = []

for x in range(amount):
    friends.append(input())


score = 0
for x in range(rounds):
    for y in range(amount):
        score += svenscore(sven[x], friends[y][x])

print(score)

maxscore = 0
for x in range(rounds):
    score1 = 0
    score2 = 0
    score3 = 0
    for y in range(amount):
        score1 += svenscore("R", friends[y][x])
        score2 += svenscore("S", friends[y][x])
        score3 += svenscore("P", friends[y][x])

    maxscore += max(score1, score2, score3)

print(maxscore)