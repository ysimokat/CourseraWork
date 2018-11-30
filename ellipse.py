
import math
import random

def printIntro():
        print("An ellipse is a curve in a plane surrounding two focal points such that the sum of the distances \nto the two focal points is constant for every point on the curve.")
        print("We  will need two focal points and a point on the curve to calculate the area of the ellipse and the circumference of the ellipse.")
        print("In this assignment we will use a Monte Carlo Simulation to estimate the overlap between two Ellipses.")

class ellipse:
    '''class that represents the necessary information of an ellipse'''

    #defining constructor
    def __init__(self,f1_x,f1_y,f2_x,f2_y,p_x,p_y):
        '''initialize ojbjects, two focal points and one point p on curve'''
        self.f1_x = f1_x
        self.f1_y = f1_y
        self.f2_x = f2_x
        self.f2_y = f2_y
        self.p_x = p_x
        self.p_y = p_y

    def setf1x(self,x1):
        '''set first focal point x coordinate'''
        self.f1_x = x1

    def setf1y(self,y1):
        '''set first focal point y coordinate'''
        self.f1_y = y1
    
    def setf2x(self,x2):
        '''set second focal point x coordinate'''
        self.f2_x = x2

    def setf2y(self,y2):
        '''set second focal point y coordinate'''
        self.f2_y = y2

    def setpx(self,x):
        '''set x coordinate of the point on the curve'''
        self.p_x = x

    def setpy(self,y):
        '''set y coordinate of the point on the curve'''
        self.p_y = y

    def get_distance(self):
        '''get distance'''
        #get the line segment PF1,PF2
        PF1 = abs(math.sqrt((self.f1_x-self.p_x)**2+(self.f1_y-self.p_y)**2))
        PF2 = abs(math.sqrt((self.f2_x-self.p_x)**2+(self.f2_y-self.p_y)**2))
        distance = PF1 + PF2
        return distance

    
    def get_a(self,dis):
        '''get the major radius'''
        return dis /2 

    def get_delta(self,a):
        '''The delta tells us how much longer a is than line segment F1F2'''
        f1f2 = abs(math.sqrt((self.f1_x-self.f2_x)**2+(self.f1_y-self.f2_y)**2)) 
        delta = (1/2)*(2*a - f1f2)
        return delta

    def get_theta(self):
        'get the angel'
        F1 = [self.f1_x,self.f1_y]
        F2 = [self.f2_x,self.f2_y]
        product = sum(i * j for i,j in zip(F1,F2))
        f1_norm = math.sqrt(self.f1_x**2+self.f1_y**2)
        f2_norm = math.sqrt(self.f2_x**2+self.f2_y**2)
        theta = math.acos(product/(f1_norm*f2_norm))
        #print(product,f1_norm,f2_norm,theta)
        return theta

    def get_v1v2(self,theta,delta):
        '''get the vertices V1 and V2'''
        v1 = (self.f1_x+delta*math.cos(theta),self.f1_y+delta*math.sin(theta))
        v2 = (self.f2_x-delta*math.cos(theta),self.f2_y-delta*math.sin(theta))
        return v1,v2

    def get_center(self,v1,v2):
        '''get the center point of the ellipse'''
        center_point = ((v1[0]+v2[0])/2,(v1[1]+v2[1])/2)
        return center_point[0],center_point[1]

    def get_b(self,x,y,a):
        ''' get the minor radius'''
        c = math.sqrt((x-self.f1_x)**2+(y-self.f1_y)**2)
        b = math.sqrt(a**2-c**2)
        return b

    def get_v3v4(self,x,y,b,theta):
        ''' get vertices V3 and V4 '''
        v3 = (x+b*math.cos(theta),y+b*math.sin(theta))
        v4 = (x-b*math.cos(theta),y-b*math.sin(theta))
        return v3,v4

    def area(self,a,b):
        'calculate the area of the ellipse'
        return math.pi * a * b
    
    def circumference(self,a,b):
        h =  (a-b)**2/(a+b)**2
        return math.pi*(a+b)*(1 + 3*h/(10+math.sqrt(4-3*h)))

def lst_var(x):
    '''this function will create a list of ellpise variables''' 
    dis = x.get_distance()
    a = x.get_a(dis)
    delta = x.get_delta(a)
    theta = x.get_theta()
    v1,v2 = x.get_v1v2(theta,delta)
    cx,cy = x.get_center(v1,v2)
    b = x.get_b(cx,cy,a)
    v3,v4 = x.get_v3v4(cx,cy,b,theta)
    return a,b,cx,cy,v1,v2,v3,v4

def compute_box(s1,s2):
    ''' compute a box/rectangle and return the length and the width of the rectangle, min/max x-axis,min/max y-axis'''
    #v1= s1[4],v2=s1[5]
    #find minumum x coordinate and maximum x coordinate
    min_x = min(s1[4][0],s1[5][0],s1[6][0],s1[7][0],s2[4][0],s2[5][0],s2[6][0],s2[7][0])
    max_x = max(s1[4][0],s1[5][0],s1[6][0],s1[7][0],s2[4][0],s2[5][0],s2[6][0],s2[7][0])
    #find minumum y coordinate and maximum y coordinate
    min_y = min(s1[4][1],s1[5][1],s1[6][1],s1[7][1],s2[4][1],s2[5][1],s2[6][1],s2[7][1])
    max_y = max(s1[4][1],s1[5][1],s1[6][1],s1[7][1],s2[4][1],s2[5][1],s2[6][1],s2[7][1])
    #calculate length and width of the rectangle
    x = max_x + min_x
    y = max_y + min_y
    #return the length and the width of the rectangle, min/max x-axis,min/max y-axis
    return x,y,min_x,min_y,max_x,max_y


def simN(n,x1,x2,y1,y2):
    '''create n points within the rectangle'''
    d = []
    for i in range(n):
        #random.uniform(x1,x2)  get a random number between x1<x<x2
        #random.uniform(y1,y2)   get a random number between y1<y<y2
        (x,y)=(random.uniform(x1,x2),random.uniform(y1,y2))
        if (x,y) not in d:
            d.append((x,y))
    #a list contain n random points
    return d

def simO(points,s1,s2,n,rec):
    '''check if the points in the overlap '''
    a,b,cx,cy,v1,v2,v3,v4 = s1
    a1,b1,c1x,c1y,v11,v12,v13,v14 = s2
    success = 0
    for i in points:
        q1 = (i[0]-s1[2])**2/s1[0]**2 + (i[1]-s1[3])**2/s1[1]**2
        q2 = (i[0]-s2[2])**2/s2[0]**2 + (i[1]-s2[3])**2/s2[1]**2
        #if (x-cx)^2/a^2+(y-cy)^2/b^2=1 at center(cx,cy)
        if q2<=1 and q1<=1:
            success += 1  #overlap
    if success == 0:
        return 0  #no overlap
    else:
        return (success /n) * rec
        

def main():
    #introduction
    printIntro()
    #two ellipse objects
    e1 = ellipse(2,3,4,3,3,5)
    e2 = ellipse(3,4,6,4,6,7)

    #create a ellipse lists [a,b,cx,cy,v1,v2,v3,v4]
    print('Function Name: {}'.format(lst_var.__name__))
    print('The docstring of the function: {}'.format(lst_var.__doc__))
    print("#create a ellipse : [a,b,cx,cy,v1,v2,v3,v4]")
    s1 = lst_var(e1)
    print('first ellipse: {}'.format(s1))
    s2 = lst_var(e2)
    print('second ellipse: {}'.format(s2))

    #compute box
    print('Function Name: {}'.format(compute_box.__name__))
    print('The docstring of the function: {}'.format(compute_box.__doc__))
    x,y,x1,y1,x2,y2 = compute_box(s1,s2)
    print("variables of the rectangle: {},{},{},{},{},{}".format(x,y,x1,y1,x2,y2))
    #estimate the area of the box/rectangle
    rec = x * y
    print("rectangle area: {}".format(rec))
    #set n = 10000, generate n random points in the rectangle
    n = 10000
    print("generate n times: {}".format(n))
    print('Function Name: {}'.format(simN.__name__))
    print('The docstring of the function: {}'.format(simN.__doc__))
    p = simN(n,x1,x2,y1,y2)
    print("random n points: {}".format(p))

    #estimate how many times random points in the ellipse and return the overlap area 
    print('Function Name: {}'.format(simO.__name__))
    print('The docstring of the function: {}'.format(simO.__doc__))
    over_A = simO(p,s1,s2,n,rec)
    print("the are of overlap: {}".format(over_A))


if __name__ == "__main__":
    main()

    
   
