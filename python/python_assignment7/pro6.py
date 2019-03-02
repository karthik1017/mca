class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __mul__(self, other):
        return (self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)

real=int(input("Enter real part of complex No") )
imag=int(input("Enter imaginary part of complex No") )
A = complex(real,imag)
real=int(input("Enter real part of complex No") )
imag=int(input("Enter imaginary part of complex No") )
B = complex(real,imag)

print ("Multiplication: " ,A*B)
