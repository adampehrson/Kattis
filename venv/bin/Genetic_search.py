def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


while True:
    data = input()
    if data == "0":
        break

    mylist = ["A", "C", "G", "T"]
    data = data.split()
    string_s = data[0]
    string_l = data[1]

    out = list()

    out.append(occurrences(string_l, string_s))

    second_number = 0
    second_number_list = list()
    third_number = 0
    third_number_list = list()
    for x in range(len(string_s)):
        tempstr = string_s[:x] + string_s[x+1:]
        if tempstr not in second_number_list:
            second_number += occurrences(string_l,tempstr)
            second_number_list.append(tempstr)
        for y in mylist:
            third_temp_str = string_s[:x] + y + string_s[x:]
            if third_temp_str not in third_number_list:
                third_number += occurrences(string_l, third_temp_str)
                third_number_list.append(third_temp_str)

    for y in mylist:
        third_temp_str = string_s + y
        if third_temp_str not in third_number_list:
            third_number += occurrences(string_l, third_temp_str)
            third_number_list.append(third_temp_str)


    print("{} {} {}".format(out[0], second_number, third_number))