import sys

while True:
    amount = int(input())
    if amount == 0:
        break
    bits = []
    for x in range(32):
        bits.append(-1)
    for y in range(amount):
        instruction = input().split()
        for x in range(1, len(instruction)):
            instruction[x] = int(instruction[x])
        if instruction[0] == "SET":
            bits[instruction[1]] = 1
        if instruction[0] == "CLEAR":
            bits[instruction[1]] = 0
        if instruction[0] == "OR":
            if bits[instruction[1]] == 1 or bits[instruction[2]] == 1:
                bits[instruction[1]] = 1
            elif bits[instruction[1]] == -1 or bits[instruction[2]] == -1:
                bits[instruction[1]] = -1
            else:
                bits[instruction[1]] = 0
        if instruction[0] == "AND":
            if bits[instruction[1]] == 0 or bits[instruction[2]] == 0:
                bits[instruction[1]] = 0
            elif bits[instruction[1]] == -1 or bits[instruction[2]] == -1:
                bits[instruction[1]] = -1
            else:
                bits[instruction[1]] = 1
    for x in range(len(bits)):
        if bits[x] == -1:
            bits[x] = "?"
        else:
            bits[x] = str(bits[x])
    bits.reverse()
    print("".join(bits))