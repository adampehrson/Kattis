amount = int(input())

passwords = []

for x in range(amount):
    temp = input().split()
    temp[1] = float(temp[1])
    passwords.append(temp)


passwords = sorted(passwords, key = lambda x: x[1])
passwords.reverse()

out = 1
current = 1
i = 1
while i < len(passwords):
    current = current - passwords[i-1][1]
    out +=  current
    i += 1

print(out)