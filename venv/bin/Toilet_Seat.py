def always_up(data):
    out = 0
    if data[0] != data[1]:
        out += 1
    if data[1] == "D":
        out += 1

    if len(data) > 2:
        return data[2:].count("D")*2 + out
    else:
        return out



def always_down(data):
    out = 0
    if data[0] != data[1]:
        out += 1
    if data[1] == "U":
        out += 1

    if len(data) > 2:
        return data[2:].count("U")*2 + out
    else:
        return out



def as_preferred(data):
    if len(data) == 2:
        if data[0] != data[1]:
            return 1
        else:
            return 0
    if data[0] != data[1]:
        return as_preferred(data[1:]) + 1
    return as_preferred(data[1:])



preferances = input()

print(always_up(preferances))
print(always_down(preferances))
print(as_preferred(preferances))