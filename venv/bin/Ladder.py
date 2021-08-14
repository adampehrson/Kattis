import math

a = list(map(int, input().split(' ')))


c = a[0]/math.sin(math.pi*a[1]/180)
print(int(c)+1)
