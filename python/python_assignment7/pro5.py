    class bank():
	balance=0;
	count=0;
	def __init__(self,accno):
		self.accno=accno
	def deposite(self,amount):
		self.balance+=amount;
		self.count+=1
		print(self.count,"). ",amount,"Credited Sucessfuly \n")
	def withdraw(self,amount):
		if self.balance-amount<0:
			self.count+=1
			print(self.count,"). ","Insuficient balance\n")
			
			pass
		else:
			self.balance-=amount;
			self.count+=1
			print(self.count,"). ",amount,"debited Sucessfuly \n")

	def display(self):
		print(self.balance,"is the actual balance\n\n")


choice='y'
while choice!='n':
	accno=int(input("Enter the account number"))
	accno=bank(accno)
	choice1='y'
	while choice1!='n':
		t=int(input("\n\nEnter your choice from the below\n1.Balance enquiry\n2.Deposit\n3.Withdraw\n\n"))
		print("\n\nTransaction Details\n")
		if(t==1):
			accno.display();
		elif(t==2):
			amount=int(input("Enter the amount : "))
			accno.deposite(amount)
			accno.display();
		elif(t==3):
			amount=int(input("Enter the amount : "))
			accno.withdraw(amount)
			accno.display();

		choice1=input("Do you like to continue : ")
