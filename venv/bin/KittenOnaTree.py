class Branch:
    def __init__(self, a):
        self.start = a[0]
        self.to = [i for i in a[1:]]


spot = input()
paths = []

while True:
    x = input()
    if x == '-1':
        break
    paths.append(Branch(x.split()))

out = spot
while True:
    temp = 'pfem'
    for x in paths:
        if spot in x.to:
            temp = x.start
    if temp == 'pfem':
        break
    out = out + ' ' + temp
    spot = temp

print(out)