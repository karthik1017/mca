# 2. Find the sum of the numbers in a list.

array = input('enter the numbers seperated by comma: ').split(',')
def sum_list(array):
    sum = 0
    for i in array:
        sum += int(i)
    return sum

print('the sum of the given array = ',sum_list(array))