from itertools import combinations
import itertools

cases = int(input())

for x in range(cases):
    out = []
    numbers = list(map(int, input().split()))[1:]
    mysums = dict()
    broken = False
    for y in range(1, 20):
        all_possible = [comb for comb in combinations(numbers, y)]
        for z in all_possible:
            if sum(z) not in mysums:
                mysums.update({sum(z): z})
            else:
                out.append(mysums[sum(z)])
                out.append(z)
                broken = True
            if broken:
                break
        if broken:
            break


    print("Case #{}:".format(x+1))
    for y in out:
        temp = ""
        for z in y:
            temp += str(z) + " "
        print(temp[:-1])