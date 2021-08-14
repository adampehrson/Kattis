data = list(map(float, input().split()))

leak = data[0]
rate = data[1]
duration = data[2]
observed_time = data[3]
water_level = data[4]


out = []

if water_level < leak:
    out.append(water_level)
    out.append(water_level)

elif water_level > leak:
    pass

