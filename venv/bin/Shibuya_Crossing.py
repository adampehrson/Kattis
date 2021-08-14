

data = list(map(int, input().split()))


people = []
i = 0
while i < data[0]:
    people.append([False]*data[0])
    i += 1


for x in range(data[1]):
    crossings = list(map(int, input().split()))
    people[crossings[0]-1][crossings[1]-1] = True
    people[crossings[1]-1][crossings[0]-1] = True


for x in people:
    print(x)