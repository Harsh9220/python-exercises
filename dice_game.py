import random

def roll_dice():
    '''Simulate rolling a six-sided dice.'''
    return random.randint(1,6)


def main():
    '''The Main function to run the Dice Game.'''
    
    print("\n------Welcome to Dice Game------")
    while True:
        print("\nEnter 1 to Roll the Dice.\nEnter 0 for exit.")
        user_choice=input(">").strip()
        
        if user_choice=="1":
            rolled_number=roll_dice()
            print(f"\nYou rolled a {rolled_number}.")
            
        elif user_choice=="0":
            print("\n--Thank you for Playing--")
            break
        else:
            print("\nInvalid input!!")
            

if __name__ == "__main__":
    main() 