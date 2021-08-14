a = input().split()

data = int(a[1]) - int(a[0])

if data > 1:
    print('Dr. Chaz will have ' + str(data) + ' pieces of chicken left over!')

elif data == 1:
    print('Dr. Chaz will have ' + str(data) + ' piece of chicken left over!')

elif data == -1:
    print('Dr. Chaz needs ' + str(data * -1) + ' more piece of chicken!')
else:
    print('Dr. Chaz needs ' + str(data*-1) + ' more pieces of chicken!')
