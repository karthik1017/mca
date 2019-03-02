import sys
array = input('list of numbers seperated by coma(,):').split(',')
def prime_numbers(array):
    print('the prime numbers from the given list are as below: ')
    for i in array:
        for j in (2,int(int(i)/2)+1):
            if not ((int(i) % j) == 0):
               break
            else :
               continue
    return
prime_numbers(array)