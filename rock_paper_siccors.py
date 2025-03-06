import random
def computer_choice():
    choices = ["rock", "paper", "scissors"]
    choice= random.choice(choices)
    print("Computer: ", choice)
    return choice

def game(player_choice, computerChoice, player_score, computer_score):
    if(player_choice=="rock"):
        if(computerChoice=="scissors"):
            player_score += 1
            print("You won")
            print("You: ", player_score, "Computer: ", computer_score )
        elif(computerChoice=="paper"):
            computer_score += 1
            print("You lost")
            print("You: ", player_score, "Computer: ", computer_score )
        elif(computerChoice=="rock"):
            print("It's a tie")
            print("You: ", player_score, "Computer: ", computer_score )
    elif(player_choice=="paper"):
        if(computerChoice=="scissors"):
            computer_score += 1
            print("You lost")
            print("You: ", player_score, "Computer: ", computer_score )
        elif(computerChoice=="rock"):
            player_score += 1
            print("You won")
            print("You: ", player_score, "Computer: ", computer_score )
        else:
            print("It's a tie")
            print("You: ", player_score, "Computer: ", computer_score )
    elif(player_choice=="scissors"):
        if(computerChoice=="rock"):
            computer_score += 1
            print("You lost")
            print("You: ", player_score, "Computer: ", computer_score )
        elif(computerChoice=="paper"):
            player_score += 1
            print("You won")
            print("You: ", player_score, "Computer: ", computer_score )
        else:
            print("It's a tie")
            print("You: ", player_score, "Computer: ", computer_score )
    return player_score, computer_score

rounds = input("Enter the number of rounds you want to play: ")
player_score = 0
computer_score = 0
for i in range(int(rounds)):
    player_choice = input("Enter your choice (rock or paper or scissors) : ").lower()
    if (player_choice.lower() == "rock" or player_choice.lower() == "paper" or player_choice.lower() == "scissors"):
        computerChoice = computer_choice()
        player_score , computer_score = game(player_choice, computerChoice, player_score, computer_score)
    else:
        print("Invalid choice. Try again")
else:
    if(player_score>computer_score):
        print("FINAL RESULT: You won")
    elif(player_score == computer_score):
        print("FINAL RESULT: It's a tie")
    else:
        print("FINAL RESULT: You lost. Better luck next time")
