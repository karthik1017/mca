# 12.Read a list of strings and display the length of each string with the string.

array = input('enter a strings seperated by comma: ').split(',')
print(array)

def length_find(str1):
    count = 0
    for i in str1:
        count = count+1
    return count

def len_count(array):
    dic = {}
    for i in array:
        dic[i] = length_find(i)
    return dic

print(len_count(array))

