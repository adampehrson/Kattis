tests = int(input())
i = 0
while i < tests:
    test = list(map(float, input().split()))
    out = [(test[0] - 1) / test[1], (test[0]) / test[1], (test[0] + 1) / test[1]]
    print(str(60*out[0]) + ' ' + str(60*out[1]) + ' ' +  str(60*out[2]))
    i += 1
