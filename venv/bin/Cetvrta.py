point1 = input().split(' ')
point2 = input().split(' ')
point3 = input().split(' ')
x = ""

if point1[0] == point2[0]:
    x = x + point3[0]
elif point1[0] == point3[0]:
    x = x + point2[0]
else:
    x = x + point1[0]
x = x + ' '
if point1[1] == point2[1]:
    x = x + point3[1]
elif point1[1] == point3[1]:
    x = x + point2[1]
else:
    x = x + point1[1]

print(x)