import random
import matplotlib.pyplot as plt
import numpy as np
print("Welcome to this mini-game, you will play againt the computer Rock paper Scissors")

#User choice!






computer_count = 0
player_count = 0
while True:
    game_list = ["Rock","Paper","Scissors"]
    player_choice = int(input("Chose 1 for Rock, 2 for Paper, and 3 for Scissors press 0 to exit: "))


    #Computer choice!

    Computer_choice = random.randint(1,3)

    #printing game results

    
    if player_choice == 0:
        break
    elif (player_choice == 1 or player_choice == 2 or player_choice == 3 ):
        print("-----------------------------------------")

        print("You chosed ",game_list[player_choice-1])
        print("Computer chosed ",game_list[Computer_choice-1])

        if (player_choice == 1):
            if (Computer_choice == 1):
                print("Draw!")
            elif (Computer_choice == 2):
                print("Computer won !")
                computer_count += 1
            elif (Computer_choice == 3):
                print("You won !")
                player_count +=1
        elif (player_choice == 2):
            if (Computer_choice == 2):
                print("Draw!")
            elif (Computer_choice == 1):
                print("Computer won !")
                computer_count += 1
            elif (Computer_choice == 3):
                print("You won !")
                player_count +=1
        elif (player_choice == 3):
            if (Computer_choice == 3):
                print("Draw!")
            elif (Computer_choice == 1):
                print("Computer won !")
                computer_count += 1
            elif (Computer_choice == 2):
                print("You won !")
                player_count +=1        
        else:
            print("ERROR")
        print(f"player score {player_count} and computer score {computer_count}")
    elif (player_choice == 4):
        x = np.array(['player count','computer count'])
        y = np.array([player_count,computer_count])
        plt.bar(x,y,width=0.2)
        plt.show()
    else:
        print("Error, Try again ! ") 

    
        
        