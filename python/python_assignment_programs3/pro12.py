n=int(input("Enter a total number of rows"))
for i in range(1,n+1):
	for x in range(n,n-i,-1):
		print(x,end="")
	print()