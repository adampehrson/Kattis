class Person:
    def __init__(self, a, b):
        self.a = a
        self.b = b


adrian = Person(0, ['A', 'B', 'C'])
bruno = Person(0, ['B', 'A', 'B', 'C'])
goran = Person(0, ['C', 'C', 'A', 'A', 'B', 'B'])


size = int(input())
word = input()

i = 0

while i < size:
    if word[i] == adrian.b[i % 3]:
        adrian.a += 1
    if word[i] == bruno.b[i % 4]:
        bruno.a += 1
    if word[i] == goran.b[i % 6]:
        goran.a += 1
    i += 1

temp = [adrian.a, bruno.a, goran.a]
temp = sorted(temp)
got = False
if temp[2] == adrian.a:
    print(adrian.a)
    got = True
    print('Adrian')
if temp[2] == bruno.a:
    if not got:
        print(bruno.a)
        got = True
    print('Bruno')
if temp[2] == goran.a:
    if not got:
        print(goran.a)
    print('Goran')
