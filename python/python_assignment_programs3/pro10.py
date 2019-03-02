n=int(input("Enter a total number of rows"))
for i in range(n,0,-1):
	str="* "
	str=str*i;
	print(""+"{:^30s}".format(str),end="")
	print()