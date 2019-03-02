# 9. Recursively convert a decimal number to binary number. Handle the exceptions.

try:
    dec = int(input('enter a decimal number to be converted: '))
except ValueError as err:
    print('not a valid input:')

def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

convertToBinary(dec)

