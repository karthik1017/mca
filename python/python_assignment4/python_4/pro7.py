try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
except ValueError as err:
    print("it is not a valid number")

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

print("GCD is: ",gcd(a,b))  
