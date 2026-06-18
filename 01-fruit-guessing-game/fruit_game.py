import numpy as np

print("WELCOME! We have a beautiful game today. You're going to like it...")

fruits = ("grape", "mango", "apple", "tangerine", "pineapple")

while True:
    user_choice = input("Guess the fruit of the day: ").lower().strip()
    computer_choice = np.random.choice(fruits)
    
    if user_choice != computer_choice:
        print("Wrong selection. It was:", computer_choice)
        inplay_options = input("Do you want to try again? yes/no: ").lower().strip()
        
        if inplay_options == "yes":
            print("OK! Let's continue...\n")
            continue
        elif inplay_options == "no":
            print("Alright! Thanks for playing. See you next time.")
            break
        else:
            print("Please select 'yes' or 'no'")
            continue
    else:
        print(f"WOW! You got it! The fruit was {computer_choice}")
        print("CONGRATULATIONS ")    
        break
