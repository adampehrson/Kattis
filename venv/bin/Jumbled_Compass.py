start = int(input())
end = int(input())

if -180 <= end - start <= 180:
    temp = end - start
    if temp == -180:
        print(180)
    else:
        print(temp)

elif end - start < -180:
    temp = 360 - start + end
    if temp == -180:
        print(180)
    else:
        print(temp)

elif end - start > 180:
    temp = -(360 - end + start)
    if temp == -180:
        print(180)
    else:
        print(temp)