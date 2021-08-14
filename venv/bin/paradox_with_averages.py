cases = int(input())

for x in range(cases):
    input()
    amounts = list(map(int, input().split()))
    computer_science = list(map(int, input().split()))
    economics = list(map(int, input().split()))
    averageiq_comp = sum(computer_science) / amounts[0]
    averageiq_eco = sum(economics) / amounts[1]
    i = 0

    for y in computer_science:
        if averageiq_eco < y < averageiq_comp:
            i += 1
    print(i)
