data = list(map(int, input().split()))
years = list(map(int, input().split()))
current = data[1]
out = ''
i = 0
while i < data[0]:
    if years[i] <= current:
        out = 'It hadn\'t snowed this early in ' + str(i) + ' years!'
        break
    i += 1

if out == '':
    print('It had never snowed this early!')
else:
    print(out)