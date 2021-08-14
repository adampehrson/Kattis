amount = int(input())
top_bottom = 0
left_right = 0

for x in range(amount):
    temp = input()

    top_bottom_temp = [y for y in temp[:2] if y == "0"]
    left_right_temp = [y for y in temp[2:] if y == "0"]

    top_bottom += len(top_bottom_temp)
    left_right += len(left_right_temp)


if top_bottom < left_right:
    out = top_bottom // 2
else:
    out = left_right // 2

print("{} {} {}".format(out, top_bottom - 2*out, left_right - 2*out))