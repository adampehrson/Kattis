cases = int(input())

for x in range(cases):
    recording = input().split()
    sounds = []

    knowledge = input().split()
    while knowledge != ['what', 'does', 'the', 'fox', 'say?']:
        sounds.append(knowledge[-1])
        knowledge = input().split()


    out = []
    for y in recording:
        if y not in sounds:
            out.append(y)

    finalout = ""
    for y in out:
        finalout = finalout + y + " "
    print(finalout[:-1])