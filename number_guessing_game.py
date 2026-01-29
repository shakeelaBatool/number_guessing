import random

def number_guess():
    com_guess =random.randint(1, 100)
    print("Computer has chosen a number between 1 and 100.")
    
    while True:
        try:
            user_guess =int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_guess < com_guess:
            print("Low guess, try again!")
        elif user_guess > com_guess:
            print("High guess, try again!")
        else:
            print("Congratulations! Your guess matches the number.")
            break
        return user_guess

# Start the game
number_guess()


