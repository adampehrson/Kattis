def smallest(myword):
    myword = myword[::-1]
    current_smallest = myword
    for x in range(len(myword)):
        if myword[x:] < current_smallest:
            current_smallest = myword[x:]
    return current_smallest



word = input()

outint = smallest(word[:-2])

outint += smallest(word[len(outint):-1])
outint += word[len(outint):][::-1]
print(outint)
