cases = int(input())

for x in range(cases):
    numb = input()
    maxones = 0
    for y in [int(numb[:x+1]) for x in range(len(numb))]:
        temp = str(bin(y))
        temp = temp.count("1")
        if temp > maxones:
            maxones = temp
    print(maxones)

