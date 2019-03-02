# 6. Read a string and check if the string contains at least one occurrence of all the 26 alphabets.

str1 = str(input('enter a string to check for pangram: '))

def pangram(str1):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    str1 = set(str1)
    if len(str1) == 26:
        print(str1,' the given string is pangram: ')
    else:
        print(str1,' is not a pangram')
pangram(str1)