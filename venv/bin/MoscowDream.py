a = list(map(int, input().split()))

if a[0] == 0 or a[1] == 0 or a[2] == 0:
    print('NO')
elif a[0] + a[1] + a[2] < a[3]:
    print('NO')
elif a[3] < 3:
    print('NO')
else:
    print('YES')