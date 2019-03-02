#1 
a=int(input("Enter a no"))
fun=lambda x:a*a
print(fun(a))

#2
exp= lambda x,y,z,p:x+y*z/p;
print(exp(4,3,4,3))

#3
lis=[2,4,3,5,6,7,8]
nw=list(filter(lambda x:(x%3!=0),lis))
print(lis)

#4
myl=[3,4,5,None,7]
while not myl[-1]:
    myl.pop()
print(myl)

#5
names=['karthik','James','Commando']
out=[name for name in names if(name[0]=='J')]
print(out)

#6
lis=[2,4,3,5,6]
nwlist=list(map(lambda x:x*x,lis))
print(nwlist)

#7
lis=['b','s','f','g','a','b','e','i']
nw=list(filter(lambda x:(x in 'aeiou'),lis))
print(nw)

#1
lis=['k','l','e','r','w','l','e']
nw=list(filter(lambda x:(x not in 'aeiou'),lis))
print(nw)

#3
lis="karthik"
newlis=[i.upper() for i in lis if(i.islower())]
print(newlis)

#4
lis="KARTHIK"
newlis=[i.lower() for i in lis if(i.isupper())]
print(newlis)

#6
lis1=[2,3,4,5,7,8]
lis2=[3,6,9,1,5,6]
nwlis=[lis1[i] + lis2[i] for i in range(0, len(lis1))]
print(nwlis)

#7
lis=['karthik','devaraj']
lis1=[]
for n in lis:
    lis1.append((len(n)))
print(lis1)

#8
lis=['karthik']
var=lis
print(var[0],var[-1])

#9
lis=['karthik','devaraj']
print(lis[::-1])

#10
my_list=[]
for drink in ['water','tea','juice']:
    for food in ['ice cream','chocolates','strawberry']:
        my_list.append([drink,food])
print(my_list)

#11
newlis=[i*i for i in range(0,10) if((i*i)>5 and (i*i)<50)]
print(newlis)

#12
newlis=['karthik','devaraj']
nw=[i for i in newlis if i[0] in 'aeiou']
print(nw)