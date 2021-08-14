first_int = input()
operand = input()
second_int = input()


if operand == "*":
    temp = len(first_int) + len(second_int) - 2
    out = "1"
    for x in range(temp):
        out += "0"
    print(out)

if operand == "+":
    print(int(first_int) + int(second_int))
