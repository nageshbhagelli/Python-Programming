# 18. Create a program to simulate a "high-low" number guessing game. The program generates 
# a random number, and the user must guess whether the next number will be higher or lower.

import random

def high_low_game():
    score = 0
    current_number = random.randint(1, 100)
    
    while True:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be higher (h) or lower (l)? ").lower()
        
        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")
        
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            score += 1
            print("You guessed correctly!")
        else:
            print("You guessed incorrectly.")
            break
        
        current_number = next_number
    
    print(f"Your final score is: {score}")

# Start the game
high_low_game()
