# 8. Read a list of numbers and display the even numbers and odd numbers separately. Sum the even numbers and odd numbers and display the same

numbers = input('enter the list of numbers seperated by comma: ').split(',')
even = []
odd = []
even_sum = 0
odd_sum = 0
for i in numbers :
  if int(i) % 2 == 0 :
      even.append(i)
  else :
      odd.append(i)
for i in even :
   even_sum += int(i) 
print(even,'=',even_sum)
for i in odd :
   odd_sum += int(i)
print(odd,'=',odd_sum)