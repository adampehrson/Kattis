tests = int(input())
for x in range(tests):
    a = list(map(int, input().split()))
    i = 2
    numb = a[1]
    while i < len(a):
        numb += 1
        if numb != a[i]:
            print(i)
            break
        i += 1
