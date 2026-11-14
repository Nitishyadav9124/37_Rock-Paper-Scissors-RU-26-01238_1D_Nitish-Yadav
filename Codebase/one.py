
import random

#for random choice of computer
def get_comp_choice(round_num):
    choices = ["scissors","rock","paper"]
    return choices[round_num - 1]

#for winners
def get_winner(player,computer):
    if player == computer:
        return "Draw"
    elif (player =="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player =="paper" and computer=="rock"):
        return "You win"
    else:
        return "Computer win"



def play_game():
    player_score = 0
    computer_score = 0
    draws = 0

    round_num =1
    while round_num <=3:
        print(f"\n======Round {round_num}======")
        player_choice = input("Enter rock, paper or scissors:").strip().lower()

        if player_choice not in ["rock","paper","scissors"]:
            print("Invalid choice. Enter rock, paper or scissors:")
            continue

        computer_choice = get_comp_choice(round_num)
        print(f"Computer choice: {computer_choice}")

        result = get_winner(player_choice , computer_choice)
        print(f"Round {round_num}: {result}")


       # score update
        if result == "You win":
            player_score +=1
        elif result == "Computer win":
            computer_score +=1
        else:
            draws +=1

        round_num +=1



    print("\n==============================================")
    print(f"You score {player_score} | Computer {computer_score} | Draws {draws}")


    if player_score > computer_score:
        print("Result: You win the match!")
    elif computer_score > player_score:
        print("Result: Computer wins the match.")
    else:
        print("Result: Match drawn.")

    print("==============================================")


while True:
    play_game()
    again = input("\nPlay again! (y/n):").strip().lower()

    if again != "y":
        print("Thanks for playing!")
        break
