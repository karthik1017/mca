n=int(input("Enter a total number of rows"))
x=1
for i in range(1,n+1):
	str1=""
	for j in range(1,i+1):
		str1=str(x)+" "+str1
		x=x+1
	print("{:>25s}".format(str1),end="")
	print()
