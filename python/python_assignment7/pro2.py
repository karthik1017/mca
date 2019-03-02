class time():
	def gettime(self):
		self.time_sec=int(input("Enter time in seconds : "))

	def hours(self):
		self.hour=int(self.time_sec/3600)
		self.time_sec=self.time_sec%3600

	def min(self):
		self.minu=int(self.time_sec/60)
		self.time_sec=self.time_sec%60

	def secs(self):
		self.sec=self.time_sec

	def display(self):
		print("Time in HH:MM:SS Format %d:%d:%d" %(self.hour,self.minu,self.sec))

t1=time()
t1.gettime()
t1.hours()
t1.min()
t1.secs()
t1.display()


