cases = int(input())

papers = list(map(int,input().split()))

papers.insert(0,0)

diff = 1
side = 0
out = 0
i = 1
broken = False
while i < len(papers):
    diff = 2*diff
    side = side/2 + 2 ** ((-2*i - 5) / 4)
    if diff > papers[i]:
        out += papers[i] * side
        diff = diff - papers[i]
    elif diff == papers[i]:
        out += papers[i] * side
        diff = 0
        print(out)
        break
    else:
        out += diff * side
        print(out)
        diff = 0
        break
    i += 1


if diff > 0:
    print('impossible')



