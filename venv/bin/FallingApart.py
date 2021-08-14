a = input()
numb = list(map(int, input().split()))
numb.sort()
alice = 0
bob = 0
i = 0
for x in reversed(numb):
    if i % 2 == 0:
        alice = alice + x
    if i % 2 == 1:
        bob = bob + x
    i += 1
print(str(alice) + ' ' + str(bob))
