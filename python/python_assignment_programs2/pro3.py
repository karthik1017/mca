# 3. Read the list of fruits and perform the following:
#If number of fruits are more than 4, add one more fruit and display 'EXCELLENT'. If banana is
#in list, change any one fruit and display 'GOOD'. If apple is in list, delete any one fruit and
#display 'AVERAGE' otherwise 'BAD'

fruits = input("enter the fruits name sperated with comma: ").split(',')
if(len(fruits) == 4):
  fruits.append(input('pls enter another fruit name to be added: '))
  print(fruits)
  print('EXELLENT')
if('banana' in fruits):
  print(fruits)
  fruits.remove(input("enter the fruit name to be changed: "))
  fruits.append(input('pls enter new fruit name: '))
  print(fruits)
  print('GOOD')
if('apple' in fruits):
  fruits.remove(fruits.index(input("enter the fruit name to be deleted: ")))
  print(fruits)
  print('AVERAGE')
else:
  print('BAD')  

