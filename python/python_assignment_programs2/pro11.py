# 11. Check whether a string inputted by the user is representing an integer or not.

string = str(input('enter your input: '))
if string.isdigit() :
    print('yes it is representing integer: ')
else :
    print('no it is not representing integer: ')