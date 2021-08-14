while True:

    no_names = int(input())

    if no_names == 0:
        break

    names = []

    i = 0
    while i < no_names:
        temp = input()
        mytuple = (temp[:2], temp)
        names.append(mytuple)
        i += 1


    sorted_by_second = sorted(names, key=lambda tup: tup[0])

    for x in sorted_by_second:
        print(x[1])

    print()