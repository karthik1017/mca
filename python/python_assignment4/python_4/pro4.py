# 4. Read a string and a character and display the frequency of its occurrence in the string.

str1 = str(input('enter a string to check the freuency: '))

def frequency(str1):
    di = {}
    for i in str1:
        if i in di:
            di[i] += 1
        else :
            di[i] = 1
    return di

print('the frequency of a string = ',frequency(str1))