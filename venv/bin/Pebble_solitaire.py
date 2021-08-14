def helper(game, pos):
    if 1 <= pos < len(game):
        if game[pos + 1] == "o" and game[pos-1] == "-":
            game[pos] = "-"
            game[pos + 1] = "-"
            game[pos - 1] = "o"
        if game[pos - 1] == "o" and game[pos+1] == "-":
            game[pos] = "-"
            game[pos - 1] = "-"
            game[pos + 1] = "o"
    return game


def myrecurs(game):
    out = game.count("o")
    for x in range(len(game)):
        if game[x] == "o":
            temp = helper(game, x)
            out = temp.count("o")
            if temp != game:
                myrecurs(game)
    return out


games = int(input())

for x in range(games):
    temp = input()
    current_game = []
    for y in temp:
        current_game.append(y)
    print(myrecurs(current_game))
