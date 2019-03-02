# 5. Check whether the input is a palindrome or not.
# a. Check whether the input is integer or string and call the respective functions to check for palindrome.

n = input("Enter a element to check for palindrome:")
temp = n

def palindrome_number(a):
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
        if(temp==rev):
            print(a," is a palindrome!")
        else:
            print(a," isn't a palindrome!")

def palindrome_string(a):
    if a == reversing(a):
        print(a," is a palindrome!")
    else :
        print(a," isn't a palindrome!")
        
def reversing(str1):
    rev_str = ''
    for i in range(len(str1)-1,-1,-1):
        rev_str += str1[i]
    return rev_str

palindrome_string(n) if type(n) == str else palindrome_number(n)