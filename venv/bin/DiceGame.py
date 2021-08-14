gunnar = list(map(int, input().split()))
emma = list(map(int, input().split()))

temp = gunnar[0] + ((gunnar[1] - gunnar[0]) / 2)
temp = temp + gunnar[2] + ((gunnar[3] - gunnar[2]) / 2)

temp2 = emma[0] + ((emma[1] - emma[0]) / 2)
temp2 = temp2 + emma[2] + ((emma[3] - emma[2]) / 2)

if temp > temp2:
    print('Gunnar')
if temp2 > temp:
    print('Emma')
if temp == temp2:
    print('Tie')