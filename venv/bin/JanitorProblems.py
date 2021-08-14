from math import  sqrt
sides = list(map(int, input().split()))

semiperimeter = (sides[0] + sides[1] + sides[2] + sides[3]) / 2

print(sqrt((semiperimeter - sides[0]) * (semiperimeter - sides[1]) * (semiperimeter - sides[2]) * (semiperimeter - sides[3])))