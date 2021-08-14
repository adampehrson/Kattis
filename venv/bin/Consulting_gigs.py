




amount = int(input())
offers = list(map(int, input().split()))
offers.sort()

out = 0
previous = 31556926 * (10**3)
for x in offers[::-1]:
    time = previous - x
    if time >= 4*10**5:
        out += 4*10**5
        previous = x
    elif time >= 3*10**5:
        out += 3*10**5
        previous = x
    elif time >= 2*10**5:
        out += 2*10**5
        previous = x


print(out // (10**5))
