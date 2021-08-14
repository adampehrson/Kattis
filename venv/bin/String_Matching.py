from sys import stdin



while True:
    pattern = stdin.readline()
    if pattern == "":
        break

    text = stdin.readline()
    out = ""

    temp = len(text) - len(pattern)
    for i in range(temp+1):
        if text[i:i+len(pattern)-1] == pattern.strip():
            out = out + str(i) + " "



    if len(out) != 0:
        print(out[:-1])
    else:
        print()

