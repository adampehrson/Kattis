

a = list(map(int, input().split()))
i = 1
while i <=a [2]:
    if i % a[0] == 0 and i % a[1] == 0:
        print('FizzBuzz')
    elif i % a[0] == 0:
        print('Fizz')
    elif i % a[1] == 0:
        print('Buzz')
    else:
        print(i)
    i += 1
