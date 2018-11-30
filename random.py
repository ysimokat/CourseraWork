
import random
def choice(acct_value):
    ''' ask the user to input their bet'''
    try: 
        c= float(input("Enter how much would you like to bet: "))  #ask user for input
        if (type(c)==float)==False or c > acct_value or c < 0:      #if this is an valid input
            return choice(acct_value) #recursion call

    except:  # handling exceptions 
        return choice(acct_value)
    return c   #return an integer

def exit():
    '''ask user to input yes for continue, no for exit'''
    again= input("Sorry, you lose. Would you like to double your bet and roll a third die, enter yes or no: ")
    if again not in ['yes','no']:
        return exit()    #recursion call
    else:
        return again   

acct_value = float(100)   #set initial acount value equal $100
print("Game begin, your account has $100")  #greets user
bet = choice(acct_value)  #user place a bet of an amount of her choosing

a,b = random.choices([1,2,3,4,5,6],k=2)  #rolls two-six-sided dice and return two value
print('You rolls {},{}'.format(a,b))
score=a+b  # score is the sum of the faces of the dice
print('sum of the faces of the dice is {}'.format(score))
if score==7 or score==12:  #if she rollas a 7 or 12 she wins and doubles her bet
    win=bet*2
    acct_value = acct_value + win
    print("Congratulations! You win ${}, now your acoount has ${}".format(win, acct_value))
else:  
    d_bet = bet*2  #double bet
    if d_bet <= (acct_value-bet):  #whether the user has enough money to double her bet or not, if yes we continue
        again = exit() #function call   #give user an option: continue play or quit
        if again == 'yes':      #if user says yes  
            c = random.choice([1,2,3,4,5,6])  #roall a thrid die
            score = a+b+c  #sum three faces of the dice
            print('You rolls {}'.format(c))
            print('sum of the faces of the dice is {}'.format(score))
            if score==7 or score==12: #if all three dice sum to 7 or 12 she wins 3 times the total value of her bet
                total=(d_bet+bet)*3
                acct_value = acct_value+total
                print("Congrats! You win ${}, and now your account has ${}".format(total,acct_value))
            else:  #if she lose
                all = bet + d_bet
                acct_value = acct_value - all
                print("You lose! You lose ${}, and now your account has ${}".format(all,acct_value))
    else:
        print("Your account does not have enough money. Bye bye, thanks for your visit.")


