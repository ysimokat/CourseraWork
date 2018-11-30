
lst=[2,1,3]  # this list represent a square

def part_a(lst):
    ''' part a) this function will accecpts a list and returns true if it contain exactly 3 ints '''
    a = [] #create a list
    #check the data type of each item in lst
    for i in lst:
        if (type(i)==int)==True:   
            a.append(i)   #if the item is int,then add to list a
    if len(a)==3 and len(lst)==3:  
        return True  #the list a contains 3 ints, so the lst contains exactly 3 ints
    else:
        return False #invalid input

# print("This list cotains 3 integers: ", part_a(lst))  # print the output of the function part_a()

def part_b(lst):
    '''this function will returns true if the list is a valid representation of a square'''

    #make sure the list contains exactly 3 ints
    if part_a(lst)==True:
        # s = the height/width of the square 
        x,y,s=[i for i in lst] # define 3 variables x,y,s
       
        #x,y are positive/negtive ints, and s must be a positive int, then it is a valid representation of a square
        if s>=0:   
            return True   #it is a valid representation of a square
        else:
            return False  #the representation is not valid
    else:
        return False

# print("The representation is valid: ", part_b(lst))  #print the output of the function part_b()

def part_c(lst):
    '''the function will return the perimeter of the square'''
    
    if part_b(lst)==True:  #if the list lst representing a square
        x,y,s=[i for i in lst] # define 3 variables x,y,s
        perimeter = 4*s  #calculate the perimeter of the square
        return perimeter   
    else:
        return -1    #the input is not valid,this list fail to represent a square

#check the function part_c()
# print("Perimeter = ", part_c(lst))
  

def part_d(lst):
    '''the function will return the area of the square'''

    if part_b(lst)==True: #if the list lst representing a square
        x,y,s=[i for i in lst] # define 3 variables x,y,s
        area = s**2  #calculate the area of the square
        return area #the input is valid, so return perimeter     
    else:
        return -1  #the input is not valid,this list fail to represent a square
    
#check the function part_c()
# print("Area = ", part_d(lst))

#---------------------part e----------------------
def overlap(lst1,lst2):
    '''
    this function will accepts two lists,each representations of two different squares. Compute the area of the overlap between the two squares.
    lst1 represent square 1,lst2 represent square 2
    ''' 

    if part_b(lst1)==True and part_b(lst2)==True and lst1 != lst2:  #if the list lst1 and lst2 represents two different squares
        x1,y1,s1=[i for i in lst1]  # define 3 variables as integer
        x2,y2,s2=[i for i in lst2]  # define 3 variables as integer
    
        #the up left corner coordinate of square_1
        a1 = (x1,y1+s1)  
        #the lower right corner coordinate of square_1
        a2 = (x1+s1,y1)  
        #the up left corner coordinate of square_2
        b1 = (x2,y2+s2)  
        #the lower right corner coordinate of square_2
        b2 = (x2+s2,y2)  

        if a2[1]<=b1[1] and a1[1]>=b2[1]:  #a2.y<=b1.y and a1.y>=b2.y then there is an overlap area between  the two squares 
            dx = abs(max(a1[0],b1[0])-min(a2[0],b2[0]))   #the width of the square(overlap area)
            dy = abs(min(a1[1],b1[1])-max(a2[1],b2[1]))   #the height of the square(overlap area)
            area = dx*dy  #area of the overlap area between the two squares
            return area 
        else:   #the two different squares are seperate from each other, so no overlap area between them
            return 0  
    else:
        return -1  #the input is not valid,return -1
   
  ########### part f, test the function overlap() ###################### 
sq1 = [1,0,2]
sq2 = [2,1,5]
sq3 = [4,3,1]
sq4 = [1,5,3]
sq5 = [6,4,-3]
sq6 = [6,4,'three']

print("The overlap of " + str(sq1) + " and " + str(sq2) + " is " + str(overlap(sq1,sq2)))
print("The overlap of " + str(sq2) + " and " + str(sq3) + " is " + str(overlap(sq2,sq3)))
print("The overlap of " + str(sq2) + " and " + str(sq4) + " is " + str(overlap(sq2,sq4)))
print("The overlap of " + str(sq1) + " and " + str(sq4) + " is " + str(overlap(sq1,sq4)))
print("The overlap of " + str(sq1) + " and " + str(sq5) + " is " + str(overlap(sq1,sq5)))
print("The overlap of " + str(sq1) + " and " + str(sq6) + " is " + str(overlap(sq1,sq6)))
        