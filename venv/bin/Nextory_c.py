import sys


# simple function making list of coords. with boats
# to make main function more readable
def helper():
    player = dict()
    for y in range(data[1]):
        current_line = input()
        for z in range(len(current_line)):
            if current_line[z] == "#":
                player.update({str(z) + " " +  str(y): [True, True]})
    return player


def findresult(values1, values2):
    if True not in values1 and True not in values2:
        return "draw"
    elif True not in values1:
        return "player two wins"
    elif True not in values2:
        return "player one wins"
    else:
        return "no result"


if __name__ == '__main__':
    cases = int(sys.stdin.readline())
    for x in range(cases):
        data = list(map(int, sys.stdin.readline().split()))
        player1 = helper()
        player2 = helper()


        i = 0
        while i < data[2]:
            temp = input()
            if i % 2 == 0:
                if temp in player1:
                    player1[temp][0] = False
                if temp in player2:
                    player2[temp][0] = False
            if i % 2 == 1:
                if temp in player1:
                    player1[temp][1] = False
                if temp in player2:
                    player2[temp][1] = False
            i += 1

        first_situation = findresult([x[0] for x in player1.values()], [x[0] for x in player2.values()])
        second_situation = findresult([x[1] for x in player1.values()], [x[1] for x in player2.values()])
        if first_situation == "draw" or second_situation == "draw":
            print("draw")
        elif sorted([first_situation, second_situation]) == sorted(["player two wins", "player one wins"]):
            print("draw")
        elif first_situation == "player one wins" or second_situation == "player one wins":
            print("player one wins")
        elif first_situation == "player two wins" or second_situation == "player two wins":
            print("player two wins")
        else:
            print("draw")