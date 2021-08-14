verses = int(input())
adjective = input()

for x in range(verses):
    if x + 1 == verses:
        print("{} bottle of {} on the wall, {} bottle of {}.".format(verses - x, adjective, verses - x, adjective))
        print("Take it down, pass it around, no more bottles of {}.".format(adjective))
    else:
        print("{} bottles of {} on the wall, {} bottles of {}.".format(verses - x, adjective, verses - x, adjective))
        if x + 2 == verses:
            print("Take one down, pass it around, {} bottle of {} on the wall.".format(verses - x - 1, adjective))
        else:
            print("Take one down, pass it around, {} bottles of {} on the wall.".format(verses - x - 1, adjective))
        print()