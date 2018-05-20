import random

class Point:
    coords = list()
    weight = int

    def __init__(self, coords, w):
        (self.coords,self.weight) = (coords,w)
    def show(self):
        print(str(self.coords)+"  w="+str(self.weight))

#def generatePoints(count, weight, disp=5, center=(0, 0, 0),dimention=2):

#disp - offset
def generatePoints(count, weight, disp, center,dimention):
    points = list()
    for i in range(count):
        coords = list()

        coords.append(-1)
        for dim in range(dimention-1):
            x = random.randint(center[0] - disp, center[0] + disp)
            coords.append(x)
        points.append(Point(coords, weight))

    for i in range(count):
        print('№1', i)

        for j in range(dimention):
            print((points[i]).coords[j])


    return points

