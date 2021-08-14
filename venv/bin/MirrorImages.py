test = int(input())

for x in range(test):
    size = list(map(int, input().split()))
    image = []
    print('Test ' + str(x+1))
    for y in range(size[0]):
        image.append(input())
    for w in reversed(image):
        out = ''
        for z in reversed(w):
            out = out + z
        print(out)