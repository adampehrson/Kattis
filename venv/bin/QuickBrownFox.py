tests = int(input())

for i in range(tests):
    sentence = input()
    sentence = sentence.lower()
    missing = ''
    e = 97
    while e < 123:
        if sentence.count(chr(e)) == 0:
            missing = missing + chr(e)
        e += 1
    if missing == '':
        print('pangram')
    else:
        print('missing ' + missing)
