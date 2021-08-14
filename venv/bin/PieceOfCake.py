def cakevolume(lst):
    a = 0
    b = 0
    if 2*lst[1] > lst[0]:
        a = lst[1]
    else:
        a = lst[0] - lst[1]
    if 2 * lst[2] > lst[0]:
        b = lst[2]
    else:
        b = lst[0] - lst[2]
    return a*b*4

print(cakevolume(list(map(int, input().split()))))
