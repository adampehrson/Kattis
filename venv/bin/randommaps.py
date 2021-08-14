import random

def randommaps(x, y):
    dungeon = []
    st = ''
    for w in range(x):
        st = st + '#'
    dungeon.append(st)
    i = 2
    while i < y:
        for v in range(x):
            a = random*3
