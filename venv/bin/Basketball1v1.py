match = input()
alice = 0
barbara = 0


for i in range(len(match)):
    if match[i] == 'A':
        alice += int(match[i+1])
    if match[i] == 'B':
        barbara += int(match[i+1])

if alice > barbara:
    print('A')
else:
    print('B')

