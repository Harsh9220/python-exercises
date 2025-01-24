import random

def random_number(a,b):
    ''' Generates a random number for given range.'''
    
    random_number=random.randint(a,b)
    return random_number


def main():
    '''The Main function for number guess game.'''
    
    print("Welcome to the Number Guess Game!\n")
    while True:
        try:
            range_start=int(input("\nEnter the Start of the range (A): "))
            range_end=int(input("\nEnter the End of the range (B): "))
            if range_start>range_end:
                print("\nInvalid range!\n")
                continue
            break
        except ValueError:
            print("\nInvalid input! Enter int value only\n")
            
    secret_number=random_number(range_start,range_end)
    attempts=0
    
    while True:
        try:  
            print(f"\nEnter your Guess between {range_start} to {range_end}")
            guess_num=int(input("> "))
            attempts+=1
            
            if guess_num<range_start or guess_num>range_end:
                print(f"\nOut of bounds! Please guess a number between {range_start} and {range_end}.\n")
                continue
            
            if guess_num>secret_number:
                print("Try Again! You guessed too high\n") 
            elif guess_num<secret_number:
                print("Try Aain! You guessed too small\n")
            else:
                print(f"\nCongratulations! You guessed the correct number {secret_number} in {attempts} attempts.\n")
                break
                
        except ValueError:
            print("\nInvalid input! Enter int value only\n")


if __name__=="__main__":
    main()