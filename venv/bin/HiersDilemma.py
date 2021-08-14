a = list(map(int, input().split()))

i = a[0]
tot = 0
while i <= a[1]:
    numb = str(i)
    broken = False
    for x in numb:
        if numb.count(x) != 1:
            broken = True
            break
        if x == '0':
            broken = True
            break
        if int(numb) % int(x) != 0:
            broken = True
            break
    if not broken:
        tot += 1
    i += 1
print(tot)
