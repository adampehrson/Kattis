a = int(input())
b = int(input())

rest = b - a * (b // a)


i = 0
while i < a:
    temp = "*"
    out = temp*(b//a)
    if rest != 0:
        out = out + "*"
        rest -= 1
    print(out)
    i += 1