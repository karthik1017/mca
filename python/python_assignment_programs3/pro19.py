n=int(input("Enter a total number of rows"))
for i in range(n,0,-1):
	str1=""
	for x in range(i,0,-1):
		str1=str1+" "+str(x)
	print("{:^30s}".format(str1),end="")
	print()