data = list(map(int, input().split()))

last_n = input()
first_m = input()

first_m_int = []

for x in range(len(first_m)):
    first_m_int.append(ord(first_m[x])-97)


print(first_m_int)
original = ""
original_int = []
i = 0
while i + len(last_n) < len(first_m):
    temp = (first_m_int[i + len(last_n)] - first_m_int[i]) % 26
    original = original + chr(temp + 97)
    original_int.append(temp)
    i += 1

print(original_int)
print(original)
