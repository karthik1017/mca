
class basic_info():
	def getdata(self):
		self.name=input("Enter a name : ")
		self.id=input("Enter ID : ")
		self.age=int(input("Enter age : "))
		self.gender=input("Enter a gender : ")

class dept_info():
	def depdata(self):
		self.dept_name=input("Enter Department : ")
		self.asgnd_work=input("Enter Assigned Work : ")
		self.time_comp=input("Enter time to complete task : ")

class emp(basic_info,dept_info):
	def printdata(self):
		print("Employee Name : ",self.name)
		print("Employee ID : ",self.id)
		print("Employee Age : ",self.age)
		print("Employee Gender : ",self.gender)
		print("Department : ",self.dept_name)
		print("Assigned Work : ",self.asgnd_work)
		print("Time to complete task : ",self.time_comp)

e=emp()
e.getdata()
e.depdata()
e.printdata()