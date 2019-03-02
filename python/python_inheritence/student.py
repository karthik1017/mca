# 
class Child():
	def __init__(self,name):
		self.name = name
class Student(Child):
	def __init__(self,name,roll):
		self.roll = roll
		Child.__init__(self,name)
a = Child("karthik")
print(a.name)
b = Student("karthik",12)
print(b.name)
print(b.roll)
