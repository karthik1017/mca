# 9. Read a list of numbers and display the numbers whose sum of individual digits is an even number. 

numbers = input('enter the list of numbers seperated by comma: ').split(',')
sums = []
num_array = []
print(numbers)
for i in numbers :
    sum = 0
    for j in i :
        sum += int(j)
    sums.append(sum)
print('given number = ',numbers)
print('there sums = ',sums)
for i in sums :
    if int(i) % 2 == 0 :
       num_array.append(numbers[sums.index(i)])
if len(num_array) == 0 :
    print('no numbers have sum which give even numbers: ')
else: 
    print(num_array)
          
