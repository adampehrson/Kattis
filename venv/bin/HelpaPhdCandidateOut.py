tests = int(input())

for i in range(tests):
    a = input()
    if a == 'P=NP':
        print('skipped')
    else:
        a = list(map(int, a.split('+')))
        print(a[0] + a[1])