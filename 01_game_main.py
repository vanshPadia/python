import random

''' game of snake water and gun'''



while True:
    yes = input("Press 'y' to play, or any other key to exit: ")
    
    if yes != 'y':
        print("Exiting the game. Thanks for playing!")
        break


    computer =random.choice([-1,0,1])
    you = input('enter your choice: ')
    dictyour ={'s':1,'w':-1,'g':0}
    yourchoice =dictyour[you]
    printdict = {'s':'Snake','w':'Water','g':'Gun'}
    compudict ={1:'Snake',-1:'Water',0:'Gun'}
    print(f'your choice is : {printdict[you]}\n and computer choice is:{compudict[computer]}' )


    if (computer == yourchoice):
        print('you Draw')
    elif (computer == -1 and yourchoice == 1):
        print("you win")
    elif(computer == -1 and yourchoice == 0):
        print('you Lose')
    elif(computer  == 1 and yourchoice == -1):
        print('you Lose')
    elif(computer == 1 and yourchoice == 0):
        print('you Win')
    elif(computer  == 0 and yourchoice == 1):
        print('you Lose')
    elif(computer  == 0 and yourchoice== -1):
        print('you Win')
    else:
        print('somting went wrong')

