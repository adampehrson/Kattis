
while True:
    a = int(input())
    if a == 0:
        break
    lst1 = []
    lst2 = []

    i = 0
    while i < a:
        lst1.append(int(input()))
        i += 1

    i = 0
    while i < a:
        lst2.append(int(input()))
        i += 1
    #sorted version of list1 to give a reference
    lst3 = sorted(lst1)
    lst4 = sorted(lst2)
    i = 0
    while i < a:
        out = lst3.index(lst1[i])
        print(lst4[out])
        i += 1

    print()