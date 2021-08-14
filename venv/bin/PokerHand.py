hand = input().split()
i = 0
while i < len(hand):
    hand[i] = hand[i][0]
    i += 1
max = 0
i = 0
while i < len(hand):
    if hand.count(hand[i]) > max:
        max = hand.count(hand[i])
    i += 1
print(max)