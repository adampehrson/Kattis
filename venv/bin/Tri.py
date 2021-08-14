a = list(map(int, input().split()))

i = 0


if a[0] + a[1] == a[2]:
    print(str(a[0]) + '+' + str(a[1]) + '=' + str(a[2]))

elif a[0] - a[1] == a[2]:
    print(str(a[0]) + '-' + str(a[1]) + '=' + str(a[2]))

elif a[0] * a[1] == a[2]:
    print(str(a[0]) + '*' + str(a[1]) + '=' + str(a[2]))

elif a[0] / a[1] == a[2]:
    print(str(a[0]) + '/' + str(a[1]) + '=' + str(a[2]))

elif a[1] + a[2] == a[0]:
    print(str(a[0]) + '=' + str(a[1]) + '+' + str(a[2]))

elif a[1] - a[2] == a[0]:
    print(str(a[0]) + '=' + str(a[1]) + '-' + str(a[2]))

elif a[1] * a[2] == a[0]:
    print(str(a[0]) + '=' + str(a[1]) + '*' + str(a[2]))

elif a[1] / a[2] == a[0]:
    print(str(a[0]) + '=' + str(a[1]) + '/' + str(a[2]))
