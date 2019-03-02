# 1) Create a class to read and add two distance. Use two member functions get_distance and show_distance that reads and displays the distance in kms and mts. Use a class variable that counts the different values stored. Use add_distance to add the distances.

class Distance:
    counts = 0
    total = 0
    distance1 = 0
    distance2 = 0
    def get_distance(self):
        self.distance1 = int(input("enter the value for distance1:"))
        self.counts += 1
        self.distance2 = int(input("enter the value for distance2:"))
        self.counts += 27
    def add_distance(self):
        self.total = self.distance1 + self.distance2
    def show_distance(self):
        print("the distance one in km = ",self.distance1," the distance one in meters ",self.distance1*1000)
        print("the distance two in km = ",self.distance2," the distance two in meters ",self.distance2 * 1000 )
        print("the total distance in km = ",self.total," the distance total distance in meters",self.total*1000)

d = Distance()
d.get_distance()
d.add_distance()
d.show_distance()   