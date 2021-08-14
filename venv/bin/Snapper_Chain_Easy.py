cases = int(input())

for x in range(cases):
    data = list(map(int, input().split()))

    if (data[1] + 1) % 2**data[0] == 0:
        print("Case #{}: ON".format(x+1))
    else:
        print("Case #{}: OFF".format(x+1))
