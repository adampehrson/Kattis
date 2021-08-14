def combinenames(a, b):
    if a[-2:] == 'ex':
        return a + b
    if a[-1:] == 'e':
        return a + 'x' + b
    if a[-1:] in ['a', 'i', 'o', 'u']:
        return a[:-1] + 'ex' + b
    return a + 'ex' + b


names = input().split()

print(combinenames(names[0], names[1]))