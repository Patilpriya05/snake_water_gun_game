import random

def swg(computer,player):
    if(computer == player):
        return None
    if(computer=='s' and player=='g'):
        return True
    elif(computer=='w' and player=='s'):
        return True
    elif(computer=='g' and player=='w'):
        return True
    else:
        return False

playersum = 0
computersum = 0
matchdrawn = 0
choice = ('s','w','g')

print("\n!!!!!....._______________WELCOME_TO_SNAKE_WATER_GUN_GAME_______________.....!!!!!")

for i in range(0,10):
    player = input("\nChoose your choice ('sanke - s','water - w','gun - g') -:")
    i += 1

    computer = random.randint(0,2)
    computer = choice[computer]
    
    win = swg(computer,player)
    print("______________________________________________________________________________")
    print(f"You choose {player} and the computer choose {computer}")
    if win is None :
        print("Match Drawn.....")
        matchdrawn += 1
    elif win:
        print(f"You won this round {i} :).....")
        playersum += 1
    else:
        print(f"You loose this round {i} :(.....")
        computersum += 1
        
if(playersum > computersum):
    print(f"\nyou won total {playersum} rounds")
    print(f"\nyou loose total {computersum} rounds")
    print(f"\nyour total matchdrawn are {matchdrawn}")
    print(":) .......... YOU WON THE MATCH .......... :)")
else:
    print(f"\nyou won total {playersum} rounds")
    print(f"\nyou loose total {computersum} rounds")
    print(f"\nyour total matchdrawn are {matchdrawn}") 
    print("\n:( .......... YOU LOOSE THE MATCH .......... :(")