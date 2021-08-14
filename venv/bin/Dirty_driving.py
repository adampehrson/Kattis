data = list(map(int, input().split()))

cars = list(map(int, input().split()))
cars.sort()

temp = [0]
for x in cars[1:]:
    temp.append(x - cars[0])
cars = temp

p = data[1]
minimum_dist = data[1]

for x in range(len(cars)):
    if p*(x+1) - cars[x] > minimum_dist:
        minimum_dist = p*(x+1) - cars[x]

print(minimum_dist)
