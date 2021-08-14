import sys
from math import pi

if __name__ == '__main__':
    data = list(map(int, sys.stdin.readline().split()))
    total = pi*(data[0]**2)
    cheese = pi*((data[0] - data[1])**2)
    print((cheese/total)*100)

