tests = int(input())

i = 0
while i < tests:
    sentence = input()
    if sentence[0:10] == 'simon says':
        print(sentence[11:])
    else:
        print()
    i += 1
