data = list(map(int, input().split()))

school_classes = {}

i = 0
while i < data[2]:
    temp = {chr(65 + i): i}
    school_classes.update(temp)
    i += 1

rows = []

i = 0
while i < data[0]:
    rows.append(input())
    i += 1


columns = []

i = 0
while i < len(rows[0]):
    temp = ""
    e = 0
    while e < len(rows):
        temp = temp + rows[e][i]
        e += 1
    columns.append(temp)
    i += 1

i = 0
while i < data[1]:
    for x in columns:
        if chr(65+i) in x:
            for y in x:
                school_classes[y] = school_classes[chr(65+i)]
    i += 1


print(len(set(school_classes.values())))

