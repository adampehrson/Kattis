a = list(map(int, input().split()))

if a[0] >= 2**(a[1]+1):
    print("no")

else:
    print("yes")