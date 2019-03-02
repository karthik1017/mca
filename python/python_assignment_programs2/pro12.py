# 12. Display depending on the number of rows

n = int(input('enter number of rows: '))
for i in range(0, n):
    for j in range(0, i+1):
        print("* ",end="")
    print('\r')