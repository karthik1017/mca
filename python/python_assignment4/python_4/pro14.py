# 14.Print all prime numbers in a given range.

n = int(input('enter a range for n : '))

def prime_gen(n):
    for num in range(2,n + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
                else:
                    print(num)
   

print("Prime numbers till",n,"are:")
prime_gen(n)