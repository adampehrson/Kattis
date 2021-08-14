numb = list(map(int, input().split()))
numb.sort()
order = input()

new = [0, 0, 0]

new[order.index('A')] = numb[0]
new[order.index('B')] = numb[1]
new[order.index('C')] = numb[2]

print(str(new[0]) + ' ' + str(new[1]) + ' ' + str(new[2]))