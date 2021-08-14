numb = input()


while len(numb) != 1:
    out = 1
    for x in numb:
        if x != '0':
            out = out * int(x)
    numb = str(out)

print(numb)
