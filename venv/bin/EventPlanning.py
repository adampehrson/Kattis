info = list(map(int, input().split()))
hotelsprices = []
i = 0
while i < info[2]:
    price = int(input())
    weeks = list(map(int, input().split()))
    weeks.sort()
    if price*info[0] <= info[1] and weeks[-1] >= info[0]:
        hotelsprices.append(price*info[0])
    i += 1

hotelsprices.sort()

if len(hotelsprices) == 0:
    print('stay home')
else:
    print(hotelsprices[0])