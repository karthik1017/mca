n=int(input("Enter a total number of rows"))
for i in range(1,n+1):
	str1=str(i)
	str1=str1*i
	print("{:>30s}".format(str1),end="")
	print()