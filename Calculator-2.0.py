import time
''' DON'T COPY MY PROGRAME 
    OK
    '''

#addition
def add(n1,n2):
    return n1 + n2

#substract
def sub(n1,n2):
    return n1 - n2

#divide
def div(n1,n2):
    return n1 / n2

#multiply
def multi(n1,n2):
    return n1 * n2

#power
def power():
    n3 = int(input('\n    Enter the number: '))
    power_len = int(input('\n      How much Power: '))
    print('----------------------------')
    print('\n ',n3,'to the power',power_len,'=',n3**power_len)
    print('\n----------------------------')
    return start()

def start():
    while True:
        try:
            time.sleep(3)
            print('''
----------------------------
       --------------
       CALCULATOR 2.0
       --------------
----------------------------
Created by: Yogesh Sharma
----------------------------
	
  Select Option
  
    <1> Add
    <2> Subs
    <3> Divide
    <4> Multiply
    <5> Square
    
   Type 0 to exit
----------------------------
''')
            choice = int(input('   Enter your Choice: '))
            if choice == 0:
                print('\n----------------------------')
                exit(1)
            elif choice >= 6:
                print('''
----------------------------
      	invalid input !
----------------------------
            	''')
                return start()
            elif choice == 5:
                return power()
            else:
                pass
            n1 = int(input('\n\tFirst number: '))
            n2 = int(input('\n\tAnother number: '))
            print('----------------------------')
            if choice == 1:
                print('\n  ',n1,' + ',n2,' = ',add(n1,n2))
            elif choice == 2:
                print('\n  ',n1,' - ',n2,' = ',sub(n1,n2))
            elif choice == 3:
                print('\n  ',n1,' / ',n2,' = ',div(n1,n2))
            elif choice == 4:
                print('\n  ',n1,' × ',n2,' = ',multi(n1,n2))
            else:
                return start()
        except ValueError:
            print('\n----------------------------')
            print('You have entered a text or symbol !\nTry Again.')
            return start()

start()
