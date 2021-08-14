stars = int(input())

print(str(stars) + ':')
i = 2
while i < stars:
    if stars % (2*i - 1) == 0 or stars % (2*i - 1) == i:
        print(str(i) + ',' + str(i-1))
    if stars % i == 0:
        print(str(i) + ',' + str(i))
    i += 1