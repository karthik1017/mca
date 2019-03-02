# 4. Read a variable, find whether it is number or string. 
# If it is a string whether it is in upper case,lower case or something else.

user_input = input("enter something: ")
if user_input.isdigit():
  print("the given word is a number ")
elif user_input.isalpha():
  if user_input.isupper():
    print('the given input is string and it is Uppercase ')
  else:
    print('the given input is string and it is Lowercase ')
else:
  print('the input is something else ')