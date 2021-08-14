def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


cups = int(input())
lst = []

i = 0
while i < cups:
    cup = input().split()
    rep = []
    if RepresentsInt(cup[0]) == True:
        rep.append(int(int(cup[0]) / 2))
        rep.append(cup[1])
    else:
        rep.append(int(cup[1]))
        rep.append(cup[0])
    lst.append(rep)
    i += 1

lst.sort()
for x in lst:
    print(x[1])

