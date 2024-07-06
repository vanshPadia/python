'''start creating '''
command = ''
started = False
while (command != 'quit'):
    command =input('> ').lower()
    
    if command.lower() != 'help' and command != 'start' and command != 'stop':
        print('''
    Start - To start the car
    Stop - To stop the car
    help - To get help ''')
    elif (command == 'help'):
        print('''
    Start - To start the car
    Stop - To stop the car
    help - To get help ''')
    elif (command == 'start'):
        if started:
            print('car allready started')
        else:
            started = True
            print("car starting...")
    elif (command == 'stop'):
        if not started:
            print ('car stoped allready')
        else:
            started = False
            print("car stoping...")
    elif (command == 'quit'):
        print("Exiting the program...")
        break
    else:
        print('Invalid command. Type "help" for available commands.')   
    