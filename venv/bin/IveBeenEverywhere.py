
i = 0
x = int(input())
while i<x:
    e = 0
    cities = list()
    total = 0
    y = int(input())
    while e <y:
        newcity = input()
        if cities.count(newcity) < 1:
            total = total +1
            cities.append(newcity)
        e +=1
    print(total)
    i+=1