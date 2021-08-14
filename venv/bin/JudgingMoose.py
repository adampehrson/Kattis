data = list(map(int, input().split()))
data.sort()
if data[0] == 0 and data[1] == 0:
    print('Not a moose')

elif data[0] == data[1]:
    print('Even ' + str(data[1]*2))

else:
    print('Odd ' + str(data[1]*2))

