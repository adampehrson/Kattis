amount = int(input())

cards = list(map(int, input().split()))

representation = ""

for x in cards:
    if x % 2 == 0:
        representation = representation + "0"
    else:
        representation = representation + "1"


i = 0
while i < len(representation) - 1:
    if (int(representation[i]) + int(representation[i+1])) % 2 == 0:
        representation = representation[:i] + representation[i+2:]
        i = 0
    else:
        i += 1
print(len(representation))