import random

def get_user_choice():
    '''Function for user to input their choice of 'rock', 'paper', or 'scissors'. Ensures the input is valid'''
    while True:
        choice=input("Enter rock, paper or scissors: ").strip().lower()
        if choice in ["rock","paper","scissors"]:
            return choice
        print("Invalid choice. Please enter rock, paper or scissors.")
        
        
def get_computer_choice():
    '''Function for computer choice of 'rock', 'paper', 'scissors'. '''
    return random.choice(['rock',"paper","scissors"])


def main():
    '''The Main fucntion for rock paper scissors game.'''
    
    print("---- ROCK PAPER SCISSORS ----")
    print("     Let the game begin!         ")
    print("-----------------------------\n")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print("\n---- RESULTS ----")
    print(f"You chose:     {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    
    if user_choice==computer_choice:
        print("Outcome : It's a tie!")
    elif ( user_choice=="rock" and computer_choice=="scissors") or \
       ( user_choice=="paper" and computer_choice=="rock") or \
       ( user_choice=="scissors" and computer_choice=="paper"):
           print("Outcome : You win!")
    else:
        print ("Outcome : Computer wins!")
        
    print("-------------------\n")
    print("Thanks for playing!")
        
    
if __name__=="__main__":
        main()