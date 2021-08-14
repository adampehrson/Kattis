a = input()
b = input()

numb1 = a.count('S')
numb2 = b.count('S')

temp = numb1*numb2
out = "0"

while temp != 0:
    out = "S(" + out + ")"
    temp -= 1

print(out)