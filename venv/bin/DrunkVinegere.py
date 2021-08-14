def decrypt(a, b, n):
    out = 0
    if n % 2 == 0:
        out = ord(a) - (ord(b) - ord('A'))
    if n % 2 == 1:
        out = ord(a) + (ord(b) - ord('A'))
    if out < 65:
        out = out + 26
    if out > 90:
        out = out - 26
    out = chr(out)
    return out.capitalize()



encrypted = input()
rule = input()
out = ''

for x in range(len(encrypted)):
    out = out + decrypt(encrypted[x], rule[x], x)
print(out)
