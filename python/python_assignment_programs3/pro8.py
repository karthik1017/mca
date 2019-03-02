n=int(input("Enter a total number of rows"))

if(n%2==0):
	n=n+1
for i in range(n,0,-1):
	str="*"
	str=str*i;
	print("{:<25s}".format(str),end="")
	print()