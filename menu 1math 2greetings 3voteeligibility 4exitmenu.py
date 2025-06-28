#this is a basic menu program 1-4
print('hey whats your name')
name = input()    # take name as input in the name variable
while True:  # always make it true
    print('So hey', name ,'this is menu program, please choose from 1 - 4')  # string concatenation
    num = input()
    num = int(num)   #converts the value took by the input variable into integer
    if num == 1:            # checks if the number is 1, if yes, runs the Math quiz
        print('welcome to the Math Quiz')
        print('what is 50 - 25')
        while True:
            q1 = int(input())
            if q1 == 25:
                print('correct answer')
                break
            else:
                print('wrong, please try again')
    elif num == 2:       #elif statement, follow control
        while True:       # nested while loops to make it in a loop until write answer is answered ( given in the question )
            print('Welcome to the Program ' + name + ' its nice to see you here, if you want to quit, write exit below')
            ans = input()
            if ans == 'exit':
                print('exitted')
                break   # breaks that while loop
    elif num == 3:
        while True:
            print('welcome to the Vote eligiblity Program')
            print('please write down your age and see if you are eligible to vote')
            age = int(input())
            if age >= 18:
                print('you are eligible, exitting to the menu')
                break
            else:
                print('you are ineligible, exitting to the menu')
                break
    elif num == 4:
        print('this option will make you exit the program. if you wanna exit, type exit')
        ans1= input()
        if ans1 == 'exit':
            print('EXITTED')
            break            