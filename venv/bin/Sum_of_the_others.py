import sys

while True:
    numbers = sys.stdin.readline()
    if numbers == "":
        break
    numbers = list(map(int, numbers.split()))
    total = sum(numbers)

    for x in numbers:
        if total - x == x:
            out = x
    print(out)
