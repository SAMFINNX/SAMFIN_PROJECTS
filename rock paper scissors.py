import random


def rock_paper_scissors():
    computer_win=0
    user_win=0
    ties=0
    print("\033[1m\033[91m\tWelcome to ROCK,PAPER,SCISSORS GAME!\033[0m")
    
    while True:
        choices = random.choice(['rock', 'paper', 'scissors'])
        user_choice = input("\nEnter your choice (rock, paper, scissors) or Q to quit: ").lower()
        print("Computer chose:",choices,".")

        if user_choice == 'Q' or user_choice == 'q':
            print("\n\tThanks for playing!\n\n\tFinal Score: \nUser:",user_win,"\nComputer:",computer_win,"\nTies:",ties)
            break
        if user_choice not in ['rock','paper','scissors']:
            print("\n\tInvalid choice. Please choose rock, paper, or scissors.")
            continue

        if user_choice == choices:
            print("\n\tIt's a tie!")
            ties+=1  
        elif (user_choice == 'rock' and choices == 'scissors' or
          user_choice == 'paper' and choices == 'rock' or
          user_choice == 'scissors' and choices == 'paper'):
            print("\n\tYou win!")
            user_win+=1
        else:
            print("\n\tYou lose!")
            computer_win+=1

    print("\n\t\033[1m\033[91mThanks for playing!\033[0m]")

rock_paper_scissors()