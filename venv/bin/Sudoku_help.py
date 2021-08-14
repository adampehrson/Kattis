import itertools


def summera(wanted, numbers):
    out = [1,2,3,4,5,6,7,8,9]
    mitttal = itertools.combinations(out, numbers)
    possibilities = [x for x in mitttal if sum(x) == wanted]
    return possibilities


wanted = int(input("Summerat tal: "))
talvilliga = int(input("Antal Boxes: "))


for x in summera(wanted, talvilliga):
    print(x)

