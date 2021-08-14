cases = int(input())

for x in range(cases):
    numbers = int(input())

    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line1 = sorted(line1)
    line2 = sorted(line2)
    line1.reverse()


    out = 0
    for y in range(numbers):
        out += line2[y] * line1[y]

    print("Case #{}: {}".format(x+1, out))
