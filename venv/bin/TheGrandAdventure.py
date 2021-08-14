tests = int(input())
for x in range(tests):
    bag = []
    adventure = input()
    out = 'YES'
    for y in adventure:
        if y == '$':
            bag.append('$')
        if y == '|':
            bag.append('|')
        if y == '*':
            bag.append('*')
        if y == 't':
            if len(bag) == 0:
                out = 'NO'
                break
            if bag[-1] == '|':
                bag.pop(len(bag) - 1)
            else:
                out = 'NO'
                break
        if y == 'j':
            if len(bag) == 0:
                out = 'NO'
                break
            if bag[-1] == '*':
                bag.pop(len(bag) - 1)
            else:
                out = 'NO'
                break
        if y == 'b':
            if len(bag) == 0:
                out = 'NO'
                break
            if bag[-1] == '$':
                bag.pop(len(bag) - 1)
            else:
                out = 'NO'
                break
    if len(bag) != 0:
        out = 'NO'
    print(out)
