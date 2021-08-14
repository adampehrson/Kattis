import sys
lines = []
longest = 0
while True:
    temp = sys.stdin.readline().strip()
    if temp == "":
        break
    if len(temp) > longest:
        longest = len(temp)
    lines.append(len(temp))
    

raggedness = 0
for x in range(len(lines)):
    if x != len(lines) - 1 and lines[x] != longest:
        raggedness += (lines[x] - longest)**2

print(raggedness)
