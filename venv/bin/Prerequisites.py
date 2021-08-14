while True:
    data = list(map(int, input().split()))
    if len(data) == 1 and data[0] == 0:
        break
    out = 'yes'
    coursestaken = list(map(int, input().split()))

    for x in range(data[1]):
        category = list(map(int, input().split()))
        i = 2
        taken = 0
        while i < len(category):
            if category[i] in coursestaken:
                taken += 1
            i+=1
        if taken < category[1]:
            out = 'no'

    print(out)

