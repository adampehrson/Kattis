

vowels = ["a", "e", "i", "o", "u", "y"]

while True:
    words = int(input())
    if words == 0:
        break
    favorite = ["", -1]
    for x in range(words):
        word = input()
        doublevowel = 0
        for y in range(len(word)-1):
            if word[y] in vowels and word[y] == word[y+1]:
                doublevowel += 1
        if doublevowel > favorite[1]:
            favorite = [word, doublevowel]
    print(favorite[0])
