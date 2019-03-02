# 3. Reverse a string without using built-in function

str1 = str(input('enter a string to reversed: '))

def reversing(str1):
    rev_str = ''
    for i in range(len(str1)-1,-1,-1):
        rev_str += str1[i]
    return rev_str

print('the reversed string is = ',reversing(str1))

