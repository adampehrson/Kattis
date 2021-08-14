import sys

i = 1
for line in sys.stdin:
    key = line.split()
    note = key[0]

    out = ''

    if note == 'Ab':
        out = 'G#'
    elif note == 'G#':
        out = 'Ab'
    elif note == 'F#':
        out = 'Gb'
    elif note == 'Gb':
        out = 'F#' + out
    elif note == 'Eb':
        out = 'D#' + out
    elif note == 'D#':
        out = 'Eb' + out
    elif note == 'C#':
        out = 'Db' + out
    elif note == 'Db':
        out = 'C#' + out
    elif note == 'A#':
        out = 'Bb' + out
    elif note == 'Bb':
        out = 'A#' + out

    if out == '':
        print('Case ' + str(i) + ': ' + 'UNIQUE')
    else:
        print('Case ' + str(i) + ': ' + out + ' ' + key[1])
    i += 1
