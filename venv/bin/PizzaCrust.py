from math import pi
radius = list(map(int, input().split()))
outer = radius[0]**2*pi
inner = (radius[0] - radius[1])**2*pi

print(100 * (1 - ((outer - inner) / outer)))
