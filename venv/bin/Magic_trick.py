data = input()

out = [data.count(x) for x in data]

if max(out) == 1:
    print(1)
else:
    print(0)
