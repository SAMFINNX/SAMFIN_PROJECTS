import random
 
def guess_number():
    number_to_guess= random.randint(1,100)
    number_of_attempts=0
    guessed_number=0

    print("\033[1m\tWelcome to the Number Guessing Game\033[0m")

    print("I have randomly seleted a number between 1 to 100")
    print("Try to guess that number in as few attempts as possible")

    while guessed_number != number_to_guess:
        
        guessed_number=int(input("\nEnter a number to guess: "))
        number_of_attempts+=1
    
        if guessed_number == number_to_guess:
            print("Congratultion you guessed the number correctly in",number_of_attempts,"attempts")
            break
        elif guessed_number < number_to_guess:
            print("\nYou guessed too low, try again")
            continue
        else:
            print("\nYou guessed too high, try again")
            continue

guess_number()