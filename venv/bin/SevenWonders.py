data = input()
lst = []
lst.append(data.count('T'))
lst.append(data.count('C'))
lst.append(data.count('G'))
lst.sort()

print(lst[0]**2 + lst[1]**2 + lst[2]**2 + lst[0]*7)