import sys


cases = int(sys.stdin.readline())

for x in range(cases):
    bapc = sys.stdin.readline()
    amount = int(sys.stdin.readline())

    integer_list = input()

    left_indent = len(integer_list) - 1
    right_indent = 0
    is_reversed = False
    empty = False
    for y in bapc:
        if y == "D" and is_reversed:
            left_indent -= 1
            while left_indent >= 0 and integer_list[left_indent] != ",":
                left_indent -= 1
                if left_indent == right_indent:
                    empty = True
                    break
        elif y == "D" and not is_reversed:
            right_indent += 1
            while right_indent < len(integer_list) and integer_list[right_indent] != ",":
                right_indent += 1
                if left_indent == right_indent:
                    empty = True
                    break
        elif y == "R":
            is_reversed = not is_reversed
        #print(integer_list[right_indent+1:left_indent])

    #print("In from left:{}".format(left))
    #print("In from right:{}".format(right))
    if left_indent < right_indent:
        print("error")
    elif empty:
        print("[]")
    else:
        if not is_reversed:
            print("[" + integer_list[right_indent + 1:left_indent] + "]")
        if is_reversed:
            temp = integer_list[right_indent+1:left_indent]
            temp = temp[::-1]

            print("[" + temp + "]")