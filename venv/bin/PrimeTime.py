import math


def Maxprimefactor(n):
    out = -1
    while n % 2 == 0:
        out = 2
        n = int(n / 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            out = i
            n = int(n / i)
    if n > 2:
       out = n
    return int(out)



def nextnumb(player, num, pos):
    while num != 1:
    
        temp = Maxprimefactor(num)
        if temp > num:
            num = temp
        else:
            num = int(num / temp)
        if player[pos] > num:
            player[pos] = num
        pos = (pos + 1) % 3
    return player



print(Maxprimefactor(20))



a = int(input())
i = 0
while i < a:
    player = [100000, 100000, 100000]
    start = input().split()
    pos = 0
    if start[0] == 'O':
        pos = 0
    if start[0] == 'E':
        pos = 1
    if start[0] == 'I':
        pos = 2
    player = nextnumb(player,int(start[1]), pos)
    print(player)
    i += 1
