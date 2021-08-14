

a = input()
whitespace = 0
lower = 0
upper = 0
other = 0
for i in range(len(a)):
    if a[i] == '_':
        whitespace += 1
    elif a[i].islower() == True:
        lower += 1
    elif a[i].isupper() == True:
        upper += 1
    else:
        other += 1

total = whitespace + lower + upper + other
print(whitespace/total)
print(lower/total)
print(upper/total)
print(other/total)