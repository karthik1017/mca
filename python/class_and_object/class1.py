class Animals(object):
	species='mammal'
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def description(self):
		return "{} is {} years old ".format(self.name,self.age)
	def speak(self,sound):
		return "{} says {} ".format(self.name,sound)
d=Animals("tiger",14)
print(d.description())
print(d.speak("roar"))

#print(Animals)		
#print(Animals)
#a=Animals()
#b=Animals()
#print(a==b)
#print(type(a),type(b))