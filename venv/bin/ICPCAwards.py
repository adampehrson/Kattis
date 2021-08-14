tests = int(input())
winners = []


i = 0

while i < tests:
    team = input().split()
    if winners.count(team[0]) == 0:
        winners.append(team[0])
        print(team[0] + ' ' + team[1])
    if len(winners) == 12:
        break
    i += 1