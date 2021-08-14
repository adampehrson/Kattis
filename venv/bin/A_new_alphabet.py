mydict = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\/[]",
    "n": "[]\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\/",
    "w": "\/\/",
    "x": "}{",
    "y": "`/",
    "z": "2"
}


sentence = input()
sentence = sentence.lower()
out = ""

for x in sentence:
    if x not in mydict:
        out = out + x
    else:
        out = out + mydict[x]

print(out)