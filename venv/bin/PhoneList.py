import sys

tests = int(sys.stdin.readline())

numbers = []

for z in range(tests):
    amount = int(input())
    numbers = []
    for x in range(amount):
        numbers.append(sys.stdin.readline().strip())

    broken = False
    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            if len(numbers[x]) != len(numbers[y]):
                if numbers[x][:len(numbers[y])] == numbers[y] or numbers[y][:len(numbers[x])] == numbers[x]:
                    broken = True
                    break
        if broken:
            break


    if broken:
        print("NO")
    else:
        print("YES")

