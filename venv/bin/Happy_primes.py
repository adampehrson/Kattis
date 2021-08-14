def is_prime(n):

    if n == 1:
        return False

    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_happy(n):
    mylst = []
    temp = n
    while n not in mylst:
        temp = 0
        for x in str(n):
            temp += int(x)**2
        mylst.append(n)
        n = temp
    if 1 in mylst:
        return True
    return False



if __name__ == '__main__':
    cases = int(input())

    for x in range(cases):
        data = list(map(int, input().split()))
        if is_prime(data[1]) and is_happy(data[1]):
            print("{} {} YES".format(data[0], data[1]))
        else:
            print("{} {} NO".format(data[0], data[1]))



