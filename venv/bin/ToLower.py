cases = list(map(int, input().split()))
solved = 0

i = 0
while i < cases[0]:
    e = 0
    subsolved = 0
    while e < cases[1]:
        a = input()
        a = a[0].lower() + a[1:]
        if a.islower():
            subsolved += 1
        e += 1
    if subsolved == e:
        solved += 1
    i += 1
print(solved)