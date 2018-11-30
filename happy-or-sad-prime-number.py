
#part a
def prime(x):
    '''this function will check if the input number is prime or not and returns true if an int is prime'''
    #prime number are greater than 1
    if (type(x)==int)==True and x > 1:
        #check for factors
        for i in range(2,x): 
            if (x % i)==0:  #check to see if there exits factor
                return False   # an int is not prime
        return True # an int is prime
    else:
        return False   # it is an invalid input

# print(prime(19))   # check the function prime(x)

#part b
def happy(x):
    '''
    this function will start with a positive integer, then replace the number by the sum of squares of its digits 
    and repeat the process untill the number equals 1, then return ture
    '''

    #the number is any positive integer
    if (type(x)==int)==True and x >=0:
        #set the for loop run 1000 times
        for i in range(1000): 
            s = [int(i) for i in str(x)]  # split integer x and return an array as integer
            x= 0   #reset x = 0
            for i in range(len(s)):  #this for loop will allow us sum of the square of its digits
                x= s[i]**2 + x       
                i +=1
            if x==1:
                return True     #this number is a happy number
        return False # this number is a sad number
               
    else:
        return False #ivalid input

#check the function happy()
# print(happy(5))
# print(happy(19))

#part c
def happy_prime(x):
    ''' this function returns true if an int is a happy prime'''
    if prime(x) == True and happy(x)==True: #function prime(x) and function happy(x) are both true, then return true
        return True
    else:
        return False

#check the function happy_prime()
#print(happy_prime(5))
#print(happy_prime(13))

#part d
def happy_p():
    '''this function computes and prints the first 100 happy primes in a comma separated list '''
    
    happy=[] #create an empty list
    #prime is greater than 2 and prime is any positive integer
    for i in range(2,10000): #let's set the range from 2 to 10000    
        if happy_prime(i)==True and len(happy)<100:
            happy.append(i)
    return happy

#check the function happy_p()
print(happy_p())

#part e
def sad_p():
    '''this function computes and prints the first 100 sad primes in a comma separated list '''
    
    sad=[] #create an empty list
    #prime is greater than 2 and prime is any positive integer
    for i in range(2,10000): #let's set the range from 2 to 10000    
        if prime(i) == True and happy(i)==False and len(sad)<100:
            sad.append(i)
    return sad

#check the function happy_p()
print(sad_p())

#check the length of the two lists
#print(len(happy_p()))
#print(len(sad_p()))
