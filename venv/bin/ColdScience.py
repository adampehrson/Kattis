a = input()
temp = input().split(' ')
neg = 0

i = 0
while i < int(a):
    if int(temp[i]) < 0:
        neg += 1
    i += 1
print(neg)