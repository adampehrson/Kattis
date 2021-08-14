n = int(input())
i = 0
while i < n:
    x=int(input())
    if x%2 == 0:
        print(str(x) + ' is even')
    else:
        print(str(x) + ' is odd')
    i += 1