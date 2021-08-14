tests = int(input())

i = 0
while i < tests:
    line1 = input()
    line2 = input()
    diff = ''
    e = 0
    while e < len(line1):
        if line1[e] == line2[e]:
            diff = diff + '.'
        else:
            diff = diff + '*'
        e += 1
    print(line1)
    print(line2)
    print(diff)
    print()
    i += 1
