cases = int(input())

i = 0
while i < cases:
    days = list(map(int, input().split()))
    candles = 0
    for x in range(days[1] + 1):
        candles = candles + x
    candles = candles + days[1]
    print(str(days[0]) + ' ' + str(candles))
    i += 1