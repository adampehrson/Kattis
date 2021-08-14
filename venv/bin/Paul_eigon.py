data = list(map(int, input().split()))

if ((data[1] + data[2]) // data[0]) % 2 == 0:
    print("paul")

else:
    print("opponent")