n=int(input("Enter a total number of rows"))
for i in range(1,n*2,2):
	str="* "
	str=str*i;
	print(""+"{:^30s}".format(str),end="")
	print()