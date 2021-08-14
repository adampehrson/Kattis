a = int(input())
out = 0

i = 0
while i < a:
    seq = input()
    e = 0
    win = 1
    while e < len(seq)-1:
        if seq[e] == 'C' and seq[e+1] == 'D':
            win = 0
            break
        e += 1
    i += 1
    out = out + win

print(out)