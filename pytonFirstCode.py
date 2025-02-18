print('Hello World')

name = input("Hellow Please enter youur Name: " )

startGame =  input("Hello " + name + "you want to playy game (yes/no) " ).lower()

if(startGame == "yes"):
    print('Let start the game...')
    direction = input("You want to go which Direction (left/right/straight):").lower()
    if(direction == "left"):
        print('wroong decision is wrong, game over!...')
    elif(direction == "right"):
        print('okey, we moved to right')
        new_direction = input("Chose bridge or river (bridge/river): ").lower()
        if(new_direction == "bridge"):
            print('you WON!... Congratualtion')
        elif(new_direction == "river"):
            print('you LOSE!...')  
    elif(direction == "straight"):
        print('you are going straight, game over!...')
else:
    priint('See you Again')

