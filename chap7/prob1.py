def instructions() :
    print("Welcome to the gretest intelletual challenge of all time: Tic-Tac-Toe.") 
    print("This will be a showdown between your human brain and my silicon processor.\n\n")
    print("You will make your move known by entering a number, 0 - 8. The number")
    print("will correspond to the board position as illstrated:\n")
    print("             0 : 1 : 2")
    print("             ---------")
    print("             3 : 4 : 5")
    print("             ---------")
    print("             6 : 7 : 8")
    print("Prepare yourself, human. The ultimate battle is about to begin.\n")

instructions()
require = input("Do you require the first move? <y/n>:")
while(1):
    if require == 'y':
        move = int(input("Where will you move? <0 - 8>:"))
        if move >= 0 and move < 9:
            print("Fine..")
    else:
        break

    
    



