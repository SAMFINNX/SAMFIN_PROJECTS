import random

def rock_paper_scissors():
    print("\033[1m\033[91m\tWelcome to ROCK,PAPER,SCISSORS GAME!\033[0m")
    choices = random.choice(['rock', 'paper', 'scissors'])
    user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()
    print("Computer chose:",choices,".")

    if user_choice not in ['rock','paper','scissors']:
        print("\nInvalid choice. Please choose rock, paper, or scissors.")
        return

    if user_choice == choices:
        print("\n\tIt's a tie!")
    elif (user_choice == 'rock' and choices == 'scissors' or
          user_choice == 'paper' and choices == 'rock' or
          user_choice == 'scissors' and choices == 'paper'):
        print("\n\tYou win!")
    else:
        print("\n\tYou lose!")

rock_paper_scissors()