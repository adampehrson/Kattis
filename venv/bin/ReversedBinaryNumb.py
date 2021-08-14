a = int(input())
a = bin(a)
a = str(a)[2:]
a = a[::-1]
a = int(a, 2)
print(a)