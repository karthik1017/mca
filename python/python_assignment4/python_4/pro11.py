# 11. Find all possible divisors of a number. Count the total number and sum up all the divisors. (Use two
#  functions)

num = int(input('enter a number :'))

def find_divisor(num):
    div = []
    for i in range(1,num+1):
        if(num % i == 0):
            div.append(i)
    return div

def count_sum(array):
    sum = 0
    for i in array:
        sum+=i
    print('the count of divisors = ',len(array))
    print('the sum of divisors = ',sum)


count_sum(find_divisor(num))
