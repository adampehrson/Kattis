a = int(input())

for a in range(a):
    b = list(map(int, input().split()))
    if b[0] < b[1] - b[2]:
        print('advertise')
    elif b[0] == b[1] - b[2]:
        print('does not matter')
    else:
        print('do not advertise')