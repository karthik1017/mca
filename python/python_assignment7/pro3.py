class student():
	def getdata(self):
		self.name=input("Enter a name : ")
		self.srn=input("Enter SRN : ")
		self.gender=input("Enter a gender : ")

class std_res(student):
	def getmarks(self):
		self.isa=int(input("Enter an ISA Marks : "))
		self.esa=int(input("Enter an ESA Marks : "))
		self.total=self.isa+self.esa
		self.sgpa=self.cgpa=self.total/10

	def printdata(self):
		print();
		print();
		print();
		print();
		print("Student Details",self.name)
		print("Student name : ",self.name)
		print("Student SRN : ",self.srn)
		print("Student Gender : ",self.gender)
		print("Student ISA Marks : ",self.isa)
		print("Student ESA Marks : ",self.esa)
		print("Student total Marks : ",self.total)
		print("Student SGPA : ",self.sgpa)
		print("Student CGPA : ",self.cgpa)

c1=std_res();
c1.getdata();
c1.getmarks();
c1.printdata();
