word = input()

i = 0
out = ['', '', '', '', '']
while i < len(word):
    if i % 3 == 2:
        out[0] = out[0][:-1] + '..*..'
        out[1] = out[1][:-1] + '.*.*.'
        out[2] = out[2][:-1] + '*.' + word[i] + '.*'
        out[3] = out[3][:-1] + '.*.*.'
        out[4] = out[4][:-1] + '..*..'

    elif i == 0:
        out[0] = out[0] + '..#..'
        out[1] = out[1] + '.#.#.'
        out[2] = out[2] + '#.' + word[i] + '.#'
        out[3] = out[3] + '.#.#.'
        out[4] = out[4] + '..#..'

    else:
        out[0] = out[0] + '.#..'
        out[1] = out[1] + '#.#.'
        out[2] = out[2] + '.' + word[i] + '.#'
        out[3] = out[3] + '#.#.'
        out[4] = out[4] + '.#..'

    i += 1

for w in out:
    print(w)