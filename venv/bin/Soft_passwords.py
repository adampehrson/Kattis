password = input()
attempted_password = input()
out = False

if attempted_password == password:
    out = True


for x in range(10):
    if str(x) + attempted_password == password:
        out = True
        break
    if attempted_password + str(x) == password:
        out = True
        break

temp = ""

for x in attempted_password:
    if x.upper() != x:
        temp = temp + x.upper()
    elif x.lower() != x:
        temp = temp + x.lower()
    else:
        temp = temp + x

if temp == password:
    out = True

if out:
    print("Yes")
if not out:
    print("No")