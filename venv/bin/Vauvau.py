times = list(map(int, input().split()))
arrival = list(map(int, input().split()))

period1 = times[0] + times[1]
period2 = times[2] + times[3]
i = 0
while i < 3:

    if arrival[i] + 1 % period1 > times[0] and arrival[i] % period2 > times[2]:
        print('none')
    elif arrival[i] + 1 % period1 > times[0] or arrival[i] % period2 > times[2]:
        print('one')
    else:
        print('both')
    i += 1