# define class employee class vaiable emp to count whos initial value is 0 inside the constructor pass the name and salary and increment the employee count use an instance method that displays the total number of employees

class Employee(object):
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def increment(self):
        Employee.count += 1
        return ("employee count is ",Employee.count)
e=Employee("karthik",140000)
e1=Employee("karthik1",14000)
print(e.increment())