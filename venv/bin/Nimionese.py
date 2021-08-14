



def consonantchange(word):
    hard_consonants = ["b", "c", "d", "g", "k", "n", "p", "t"]
    dist = 30
    changeto = "b"
    for x in hard_consonants:
        tempdist = abs(ord(word[0].lower()) - ord(x))
        if tempdist < dist:
            changeto = x
            dist = tempdist
        elif tempdist >= dist:
            break

    if word[0].isupper():
        word = changeto.upper() + word[1:]
    else:
        word = changeto + word[1:]

    temp = ""
    for y in "".join(word.split("-")[1:]):
        if y in hard_consonants:
            temp += changeto
        else:
            temp += y

    word = word.split("-")[0] + temp
    return word



def vowels(word):
    hard_consonants = ["b", "c", "d", "g", "k", "n", "p", "t"]
    changeto = ""
    dist = 30
    if word[-1].lower() in hard_consonants:
        options = ["a", "o", "u"]
        changeto = "ah"
        dist = 30
        for x in options:
            tempdist = abs(ord(word[-1]) - ord(x))
            if tempdist < dist:
                changeto = x + "h"
                dist = tempdist
            elif tempdist >= dist:
                break
    return word + changeto


myword = input().split(" ")

for x in range(len(myword)):
    myword[x] = consonantchange(myword[x])
    myword[x] = vowels(myword[x])

print(" ".join(myword))
