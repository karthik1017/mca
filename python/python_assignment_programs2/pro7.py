# 7. Display depending on the number of rows.

n = int(input('enter number of rows: '))
col = 0
for i in range(0, n*2):
    for j in range(0, col):
        print("* ",end="")
    if i < n :
      col += 1
    else :
      col -= 1
    print('\r')