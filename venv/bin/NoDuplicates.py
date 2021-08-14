def duplicates(a):
    data = a.split()

    out = 'yes'
    for x in data:
        if data.count(x) > 1:
            out = 'no'
            break
    return out

print(duplicates(input()))