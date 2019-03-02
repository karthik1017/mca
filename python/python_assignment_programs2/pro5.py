# 5. Find those numbers which are divisible by 9 and multiples of 5.

number = int(input('enter the number : '))
if number%9 == 0 :
    if number%5 == 0 :
        print('the number is divisible by 9 and multiple of 5')
    else : 
        print('the number is only divisible by 9')
else:
    print('the number is not divisible by 3 and not a multiple of 9 ')
