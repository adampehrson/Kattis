from math import sqrt

data = list(map(int, input().split()))

plots = list(map(int, input().split()))
plots = [2*x for x in plots]

circular_houses = list(map(int, input().split()))
circular_houses = [2*x for x in circular_houses]

square_houses = list(map(int, input().split()))

for a in square_houses:
    circular_houses.append(sqrt(2*(a**2)))

plots.sort()
circular_houses.sort()

plots.reverse()
circular_houses.reverse()



i = 0
j = 0
while j + i < len(circular_houses) and j < len(plots):
    #print("House: {}".format(circular_houses[j+i]))
    #print("Plot: {}".format(plots[j]))
    #print("j: {}, i: {}".format(j, i))
    if circular_houses[j + i] < plots[j]:
        j += 1
    else:
        i += 1

print(j)
