amount = int(input())

mypeople = []

for x in range(amount):
    person = input().split()
    taken = False
    for y in range(len(mypeople)):
        if mypeople[y][2] == person[2]:
            taken = True
            if int(person[1]) > int(mypeople[y][1]):
                mypeople[y] = person

                break

    if not taken:
        mypeople.append(person)

sorted_by_first = sorted(mypeople, key=lambda tup: tup[0])


print(len(sorted_by_first))
for x in sorted_by_first:
    print(x[0])
