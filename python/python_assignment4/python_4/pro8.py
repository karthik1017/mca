# 8. Recursively sum up ‘n’ natural numbers

val = int(input('input range to find a sum of n natural numbers: '))

def calculate(val):
    if val == 1:
        return 1
    else:
        return val+calculate(val-1)

print('the sum of ',val,' natural numbers = ',calculate(val))