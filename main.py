import random

# create a list to store all possible options:
possible_actions = ["R", "P", "S"]

# function to assign a random possible option to the computer
def get_computer_input():
    computer_action = random.choice(possible_actions)
    return computer_action

# function to get user input
def get_user_input():
    user_action = input("Enter a choice: ")
    return user_action

# function to determine winner 
def outcome_conditions(player_outcome, computer_outcome):
    #we need to check of a draw
    if player_outcome == computer_outcome:
        print("<== Its a tie ==>")
       
    # condition for other combinations
    elif player_outcome == "R":
        if computer_outcome == "S":
            print("Rock beat scissors! You Win!")
        else:
            print("Paper beat rock! You Lose! \n Computer Wins!")
    elif player_outcome == "P":
        if computer_outcome == "R":
            print("Paper beat rock! You Win!")
        else:
            print("Scissors beat paper! You Lose! \n Computer Wins!")
    elif player_outcome == "S":
        if computer_outcome == "P":
            print("Scissors beat paper! You Win!")
        else:
            print("Rock beat scissors! You Lose! \n Computer Wins!")

while True:
    print("Enter choice \n R for rock, \n P for paper, and \n S for scissors \n")
    
    # take input from user:
    player = get_user_input()

    # looping until user enter valid input
    while player != "R" and player != "P" and player != "S":
        print("Invalid input!... Enter a valid input")
        player=get_user_input()

    # get computer input
    computer = get_computer_input()

    # initialize value of player_choice variable
    # corresponding to the player value
    if player == "R":
        player_choice = "Rock"
    elif player == "P":
        player_choice = "Paper"
    else:
        player_choice = "Scissors"

    # initialize value of computer_choice variable
    # corresponding to the computer value
    if computer == "R":
        computer_choice = "Rock"
    elif computer == "P":
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    # display user and computer input
    print(f"\nPlayer ({player_choice}) : CPU ({computer_choice}).\n")
    
    # determine winner 
    outcome_conditions(player, computer)

    #Checks for tie condition and restart game:
    if player == computer:
        print("\n Play Again!\n")
        
    else:   
        #Replay option
        ans = input("\nDo you want to play again? (y/n): ")
    
        # if user input y or Y then game is restarted
        if ans.lower() != "y":
            break #If true, Breaks out of the loop.

# we print thanks for playing after coming out of loop.
print("\nThanks for playing")