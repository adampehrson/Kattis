from sys import  stdin


while True:
    data = stdin.readline()
    if data == "":
        break
    data = data.split()

    morning_hours = int(data[3][:data[3].find(":")])
    morning_minutes = int(data[3][data[3].find(":")+1:])

    night_hours = int(data[4][:data[4].find(":")])
    night_minutes = int(data[4][data[4].find(":")+1:])

    night_hours = night_hours - morning_hours
    night_minutes = night_minutes - morning_minutes

    if night_minutes < 0:
        night_hours -= 1
        night_minutes += 60

    print("{} {} {} {} hours {} minutes".format(data[0], data[1], data[2], night_hours, night_minutes))
