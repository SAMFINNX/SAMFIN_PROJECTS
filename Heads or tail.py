import random

def heads_or_tails():
    guessed_choice = random.choice(['heads', 'tails'])

    print("\033[1m\tWelcome to the Heads or Tails Game\033[0m")
    print("I will flip a coin and you have to guess whether it will be heads or tails")

    user_guess = input("\nEnter your guess (heads/tails): ").lower()

    if user_guess not in ['heads', 'tails']:
        print("\nInvalid input. Please enter 'heads' or 'tails'.")
        return
    
    print("\nFlipping the coin...")   

    if guessed_choice == user_guess:
        print("\nCongratulations! You guessed it right. It was",guessed_choice,".")
    else:
        print("\nSorry, you guessed wrong. It was",guessed_choice,".")

heads_or_tails()