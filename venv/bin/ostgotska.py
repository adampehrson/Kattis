sentence = list(map(str, input().split()))
total = 0
for x in sentence:
    if 'ae' in x != 0:
        total += 1

percentage = 100 * total / len(sentence)
if percentage >= 40.0:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
