print("\tWelcome to the Great Quizin Show")

if input("\nPress Enter to start the game") == "":
    print("\nLet's get started!")
    print("\nYou will be asked 5 questions. Each question has 4 options. You have to choose the correct option by entering the option number (1, 2, 3, or 4).")
    
print("\nQuestion 1: What is the capital of France?")
print("1. London")
print("2. Berlin")
print("3. Paris")
print("4. Madrid")

a1 = int(input("\nEnter your answer (1-4): "))
if a1 == 3:
    print ("\nCorrect!")
else:
    print("\nIncorrect! The correct answer is 3. Paris.")

print("\nQuestion 2: What is the largest planet in our solar system?")
print("1. Earth")
print("2. Saturn")
print("3. Uranus")
print("4. Jupiter")

a2 = int(input("\nEnter your answer (1-4): "))
if a2 == 4:
    print("\nCorrect!")
else:
    print("\nIncorrect! The correct answer is 4. Jupiter.")

print("\nQuestion 3: Who wrote the play 'Romeo and Juliet'?")
print("1. William Shakespeare")
print("2. Charles Dickens")
print("3. Jane Austen")
print("4. Mark Twain")

a3 = int(input("\nEnter your answer (1-4): "))
if a3 == 1:
    print("\nCorrect!")
else:
    print("\nIncorrect! The correct answer is 1. William Shakespeare.")

print("\nQuestion 4: What is the chemical symbol for water?")
print("1.O2")
print("2.H2O")
print("3.CO2")
print("4.N2")

a4 = int(input("\nEnter your answer (1-4): "))
if a4 == 2:
    print("\nCorrect!")
else:
    print("\nIncorrect! The correct answer is 2. H2O.")

print("\nOuestion 5: Who directed the movie 'Inception'?")
print("1.Christopher Nolan")
print("2.Martin Scorsese")
print("3.Steven Spielberg")
print("4.Quentin Tarantino")

a5=int(input("\nEnter your answer (1-4): "))
if a5 == 1:
    print("\nCorrect!")
else:
    print("\nTncorrect! The correct answer is 1. Christopher Nolan.")
