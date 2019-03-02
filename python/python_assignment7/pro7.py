import math as m

class Point:
    def get_points(self):
        self.x = int(input("Enter the value of x : "))
        self.y = int(input("Enter the value of y : "))
        
    def get_distance(self,x1,y1,x2,y2):
        distance = m.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
        print("Distance between the two points : ",distance)
        
    def __gt__(self,x,y):
        if x.x > y.x and x.y > y.y:
            return True
        elif y.x > x.x and y.y > x.y:
            return True
        else:
            return False
        
    def __lt__(self,x,y):
        if x.x < y.x and x.y < y.y:
            return True
        elif y.x < x.x and y.y < x.y:
            return True
        else:
            return False
        
    def check_Quadrant(self,x1,y1,x2,y2):
        if x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0:
            print("They lie in the same quadrant")
        elif x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0:
            print("They lie in the same quadrant")
        else:
            print("They lie in different quadrants")
                
p = Point()
q = Point()
p.get_points()
q.get_points()
r = Point()
r.get_distance(p.x,p.y,q.x,q.y)
print(r.__gt__(p,q))
print(r.__lt__(p,q))
r.check_Quadrant(p.x,p.y,q.x,q.y)
