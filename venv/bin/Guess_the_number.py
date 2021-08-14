myrange = [0, 1001]

while True:
    guess = int(myrange[0] + ((myrange[1] - myrange[0])/2))
    print(guess, flush= True)
    answer = input()
    if answer == "lower":
        myrange[1] = guess
    if answer == "higher":
        myrange[0] = guess
    if answer == "correct":
        break