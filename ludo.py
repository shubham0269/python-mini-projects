
import random

print("\n welcome to the world of game : 👤")

print("="*37)

print()

player_score  = 0
computer_score = 0

while True:   
    option = range(1,7)
    player = None
    
    while player not in option:
        player = int(input("enter you choice () :  "))
        
    
    computer_choice = random.choice(option)
    print(f"computer : {computer_choice}")
    print(f"player : {player}")
    
    player_score += int(player)
    computer_score += int(computer_choice)

        
    play_again = input("play again (y/n): ").lower()
    if  play_again=="n":  
        print()
        if player_score>computer_score:
            print("❤︎"*30)
            print(f"you win the the match \nyour  score : {player_score} \ncomputer score : {computer_score} ")
            print()
        elif player_score==computer_score:
            
            print(f"ono! match is tie  \nyour  score : {player_score} \ncomputer score : {computer_score} ")
            print()
        else:
            print(f"you lose the the match \nyour  score : {player_score} \ncomputer score : {computer_score} ")
            print()           
        break
    