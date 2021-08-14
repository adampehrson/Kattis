import sys


def find_nth(haystack, needle, n):
    start = 0
    while start >= 0 and n >= 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


cases = int(sys.stdin.readline())

for x in range(cases):
    bapc = sys.stdin.readline()
    amount = int(sys.stdin.readline().strip())


    integer_list = input()

    end_atindex = amount
    start_atindex = 0
    is_reversed = False

    for y in bapc:
        if y == "D" and is_reversed:
            end_atindex -= 1
        if y == "D" and not is_reversed:
            start_atindex += 1
        if y == "R":
            is_reversed = not is_reversed

    if end_atindex < start_atindex:
        print("error")
    else:
        integer_list = integer_list[find_nth(integer_list,",", start_atindex)+1:find_nth(integer_list,",", end_atindex)]
        if not is_reversed:
            print("[" + integer_list + "]")
        if is_reversed:
            integer_list = reversed(integer_list.split(","))
            out = ",".join(integer_list)

            print("[" + out + "]")
