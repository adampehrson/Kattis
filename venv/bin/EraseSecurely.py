a = int(input())
b = input()
c = input()
if a % 2 == 0:
    if b == c:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
if a % 2 == 1:
    i = 0
    fail = False
    while i < len(b):
        if b[i] == c[i]:
            fail = True
        i += 1
    if fail == False:
        print('Deletion succeeded')
    else:
        print('Deletion failed')