def complex_street(a,b,interval, letters):
    while a <= b:
        temp = str(a)
        for z in temp:
            z = int(z)
            letters[z][1] += 1
        a += interval
    return letters

def simple(a, letters):
    for z in str(a):
        z = int(z)
        letters[z][1] += 1
    return letters


def rip(total):
    if total != 1:
        return "s"
    else:
        return ""

cases = int(input())

for x in range(cases):
    letters = []
    for i in range(0,10):
        letters.append([i, 0])

    street = input()
    print(street)
    addresses = input()
    print(addresses)
    amount_addresses = int(addresses.split()[0])

    while amount_addresses != 0:
        new_addresses = input().split()
        if new_addresses[0] == "+":
            amount_addresses -= (int(new_addresses[2]) - int(new_addresses[1]) ) // int(new_addresses[3]) + 1
            letters = complex_street(int(new_addresses[1]), int(new_addresses[2]), int(new_addresses[3]), letters)
        else:
            amount_addresses -= 1
            letters = simple(new_addresses[0], letters)

    for x in range(0,10):
        print("Make {} digit {}".format(letters[x][1], x))

    total = 0
    i = 0
    while i < len(letters):
        total += letters[i][1]
        i += 1

    print("In total {} digit{}".format(total, rip(total)))

