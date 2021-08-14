original_text = input()
newtext = input()
sticky = ""


for x in original_text:
    if original_text.count(x) != newtext.count(x) and x not in sticky:
        sticky += x

print(sticky)