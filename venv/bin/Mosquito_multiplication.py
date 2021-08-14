import sys

while True:
    data = sys.stdin.readline().strip()
    if data == "":
        break

    data = list(map(int, data.split()))
    mosquitioes = data[0]
    pupae = data[1]
    larvae = data[2]
    eggs = data[3]
    proportion = data[4]
    emerged = data[5]
    weeks = data[6]

    for x in range(weeks):
        larvae_temp = mosquitioes*eggs
        pupae_temp = larvae // proportion
        mosquitioes_temp = pupae // emerged
        mosquitioes = mosquitioes_temp
        pupae = pupae_temp
        larvae = larvae_temp

    print(mosquitioes)
