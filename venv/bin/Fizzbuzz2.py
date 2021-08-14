

data = list(map(int, input().split()))


wanted = ["fizz", "buzz"]

scores = []
for x in range(data[0]):
    person = input().split()
    score = 0
    for y in range(len(person)):
        if (y+1) % 15 == 0:
            if person[y] == "fizzbuzz":
                score += 1
        elif (y+1) % 5 == 0:
            if person[y] == "buzz":
                score += 1
        elif (y+1) % 3 == 0:
            if person[y] == "fizz":
                score += 1
        else:
            if person[y] == str(y+1):
                score += 1
    scores.append(score)


print(scores.index(max(scores))+1)
