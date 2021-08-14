data = list(map(int, input().split()))

for x in range(data[2]):
    cards = list(map(int, input().split()))

    if data[1] in cards[1:]:
        print("KEEP")
    else:
        print("REMOVE")