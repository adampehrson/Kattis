time = 0
running = False
previous = 0

presses = int(input())

for x in range(presses):
    current = int(input())
    if not running:
        running = True
    else:
        running = False
        time = time + current - previous
    previous = current


if not running:
    print(time)
if running:
    print("still running")