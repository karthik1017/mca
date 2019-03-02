num = range(1,21)
even = lambda x:x%2 == 0

num = ['even' if even(i) else 'odd' for i in num]

print(num)

