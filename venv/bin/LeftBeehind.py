while True:
    a = list(map(int, input().split()))
    if a == [0,0]:
        break
    if a[0] + a[1] == 13:
        print('Never speak again.')
    elif a[0] > a[1]:
        print('To the convention.')
    elif a[1] > a[0]:
        print('Left beehind.')
    elif a[0] == a[1]:
        print('Undecided.')