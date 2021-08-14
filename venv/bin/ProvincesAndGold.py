resources = list(map(int, input().split()))
out = ''
total = resources[0]*3 + resources[1]*2 + resources[2]

if total >= 8:
    out = 'Province or '

elif total >= 5:
    out = 'Duchy or '

elif total >= 2:
    out = 'Estate or '

if total >= 6:
    out = out + 'Gold'

elif total >= 3:
    out = out + 'Silver'

else:
    out = out + 'Copper'

print(out)