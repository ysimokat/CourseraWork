
#starting word, goal word
start = 'tsudmi'
goal = 'submit'

#ask user for a name
name = input("Enter you name: ")

#greeting the user by name
print(" Hello %s , Welcome!" % (name)) 

#print instructions
print("------------Instruction-----------")
print("This game will represents the user with a starting word, then ask user to make a single change at each step untill it matches a goal word.")
print("At each step, the user has three options: a)insert a character, b)remove a character, or c)replace a character")

start1 = [i for i in start] #create a list,it contains each character of starting word
dic = {} #create a dictionary 
for i in range(len(start1)):
    dic[i] = start1[i] #add key,value into dictionary dic
print("Note: this is the starting word %s, and the index of each character is the integer " % str(start), dic)
print("When the goal word is reached, you win the game!")
print("--------Let's begin!----------")
print("--------the starting and goal words--------------")
print("Starting word= ", start)
print("Goal word= ", goal)

#creat a list, it contains 3 user options
options=['a','b','c']
def option_u():
    ''' ask user input option and handle the exceptions'''
    option = input("Please enter your choice as a, b, or c: ")  #ask user input
    if option not in options: #check if the input is valid
        return option_u() #recursion call
    return option   #return the user choice

def positions(start):
    '''ask user input the position of the character and handle exceptions'''
    try:
        position = input("Enter the index: ") #ask user input
        d = [i for i in range(0,len(start)+1)] #index range 
        if int(position) not in d: #the input is valid if the input is in d
            return positions(start)  #recursion call
    except ValueError:
        return positions(start) 
      
    return int(position) #the position of the character , or index


count = 0 #create variable count
while ((start==goal)==False):
    #user options
    print("Options: a)insert a character, b)remove a character, or c)replace a character")

    option = option_u() # user's option
    position = positions(start) #the position of the character occur

    if option=='a':   #insert a character
        char = input("Enter the character: ")
        start1.insert(position,char)   #insert a character at the index of the position
    elif option=='b':    #remove a character
        start1.pop(position)  #remove the index
       
    elif option=='c':   #replace a character
        char = input("Enter the character: ")
        start1[position]=char  #replace the index with new character
        
    else:
        continue
    count+=1  #add 1 to the count
    start=''.join(start1)  #set new word start1 as str and use start1 to replace start
    print("starting word= ", start)  #print the result

#Congratulate the user by name and output the number of steps it took to achieve the goal. 
print("Congratulations, %s ! You only took %d steps to achieve the goal!" % (name,count))



#--------------------Example------------------
# start = tsudmi
# goal = submit
# step 0: tsudmi        #starting word
# step 1: sudmi         #remove index 0
# step 2: submi         #replace index2 with 'b'
# step 3: submit        #insert 't' at index 5

        


   
