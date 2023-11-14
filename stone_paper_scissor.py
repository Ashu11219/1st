import random as r
while 1!=0:
    a=int(input('Stone(1), paper(2) or scissor(3)? '))
    x=r.randrange(1,4)
    if(a not in (1,2,3)):
        print('Enter a valid input')
        continue
    if(x==1):
        print('I put stone')
        if(a==3):
            print('I win!!! You lose')
        elif(a==1):
            print("Oops! It's a tie")
        else:
            print('You win!!!')
    elif(x==2):
        print('I put paper')
        if(a==2):
            print("Oops! It's a tie")
        elif(a==1):
            print('I win!!! You lose')
        else:
            print('You win!!!')        
    elif(x==3):
        print('I put scissors')
        if(a==3):
            print("Oops! It's a tie")
        elif(a==1):
            print('You win!!!')
        else:
            print('I win!!! You lose')
            
    
