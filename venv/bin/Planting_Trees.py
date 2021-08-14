amount = int(input())

trees = list(map(int, input().split()))

trees.sort()
trees.reverse()


out = 0
i = 0
while i < len(trees):
    if trees[i] + i + 2 > out:
        out = trees[i] + i + 2
    i += 1

print(out)