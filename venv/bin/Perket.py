import itertools


def solver(usedingredients):
    sourness = 1
    bitterness = 0
    for x in usedingredients:
        sourness = sourness*x[0]
        bitterness += x[1]
    return abs(sourness - bitterness)
ingredients = int(input())

myingredients = []
for x in range(ingredients):
    myingredients.append(list(map(int, input().split())))

out = solver(myingredients)
for x in range(1,10):
    comb = itertools.combinations(myingredients, x)
    for y in comb:
        temp = solver(y)
        if temp < out:
            out = temp
print(out)