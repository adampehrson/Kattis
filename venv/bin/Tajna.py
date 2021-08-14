import  math
coded = input()
decoded = ''

a = 1
b = 0


while True:
    if len(coded) % a == 0:
        b = int(len(coded) / a)
        if a >= b:
            break
    a += 1


i = 0
while i < b:
    e = 0
    while e < a:
        decoded = decoded + coded[e*b + i]
        e += 1
    i += 1
print(decoded)