class shape:
    get_color=""
    set_color=""
    def __init__(self,get_color,set_color='black'):
        self.get_color=get_color
        self.set_color=set_color
    def print(self):
        print("the shape color is:{} and {}".format(self.get_color,self.set_color))

class Rectangle(shape):
    get_length=""
    get_breadth=""
    set_length=""
    set_breadth=""
    get_area=""
    get_peimeter=""
    def __init__(self,get_breadth,get_length):
        self.get_length=get_length
        self.get_breadth=get_breadth
        self.set_length=self.get_length
        self.set_breadth=self.get_breadth
        self.get_area=self.set_length*self.set_breadth
        self.get_peimeter=2*(self.get_length+self.get_breadth)
    def area(self):
        print("area of rectangle is:{}".format(self.get_area))
    def perimeter(self):
        print("perimeter of rectangle is:{}".format(self.get_peimeter))

class circle(Rectangle):
    get_radius=""
    set_radius=""
    get_area=""
    get_perimeter=""
    def __init__(self,get_radius):
        self.get_radius=get_radius
        self.set_radius=self.get_radius
        self.get_area=3.14*self.set_radius*self.set_radius
        self.get_perimeter=2*3.14*self.set_radius
    def area(self):
        print("area of circle is:{}".format(self.get_area))
    def perimeter(self):
        print("perimeter of circle is:{}".format(self.get_perimeter))
s1=shape("blue")
s1.print()
r1=Rectangle(23,45)
r1.area()
r1.perimeter()
c1=circle(7)
c1.area()
c1.perimeter()