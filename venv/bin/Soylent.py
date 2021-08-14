cases = int(input())

for x in range(cases):
     a = int(input())
     i = 0
     while a > 0:
         a = a - 400
         i += 1
     print(i)