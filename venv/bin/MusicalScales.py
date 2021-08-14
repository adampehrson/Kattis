def major(a, lst):
    spot = lst.index(a)
    i = 0
    out = set()
    out.add(lst[spot % len(lst)])
    out.add(lst[(spot + 2) % len(lst)])
    out.add(lst[(spot + 4) % len(lst)])
    out.add(lst[(spot + 5) % len(lst)])
    out.add(lst[(spot + 7) % len(lst)])
    out.add(lst[(spot + 9) % len(lst)])
    out.add(lst[(spot + 11) % len(lst)])
    return out



tones = int(input())

song = input().split()

notes = set(song)

scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

out = ''

i = 0
while i < 12:
    if notes & major(scale[i], scale) == notes:
        out = out + scale[i] + ' '
    i += 1

if out == '':
    print('none')
print(out)

