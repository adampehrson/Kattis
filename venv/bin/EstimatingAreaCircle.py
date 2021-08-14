import  math

while True:
    data = list(map(float, input().split()))
    if data.count(0.0) == 3:
        break
    out = str(data[0]**2*math.pi)
    out = out + ' ' + str((data[2] / data[1])*((data[0]*2)**2))
    print(out)