'''guessing game'''
import random
while True:
    

    computer = random.randint(1,100)
    yournum =''
    count = 0
    
    while True:
        
        yournum = int(input('''Guess the Number: 
        > '''))
        if yournum == -1:
            print('exit')
            break
        
        if yournum == 0:
            print(computer)
            
        count +=1

        if computer == yournum:
            print('your guessing is correct')
            print(f'your guessed it in : {count} attempts')
            break
        elif computer > yournum:
            print('guess is smaller  ')
            print('please try another guess')
        else:
            print('guess is high  ')
            print('please try another guess')
        
    conti = input("Enter 'y' to play again, or any other key to exit: ")
    if conti.lower() != 'y':
        break
