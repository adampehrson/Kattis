data = input()

pos = 0
out = []

notallowed = ["L", "R", "B"]

for x in data:
    if x not in notallowed:
        out.insert(pos, x)
        pos += 1
    elif x == "L":
        pos -= 1
    elif x == "R":
        pos += 1
    elif x == "B":
        pos -= 1
        out.pop(pos)



final_out = "".join(out)

print(final_out)