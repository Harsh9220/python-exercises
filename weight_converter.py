def get_user_input(prompt):
    '''Prompts the user for input and ensures it's a valid number.'''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def weight_converter():
    '''The Main Weight Converter fucntion to Displays a menu to the user to convert weights.'''
    
    while True:
        print("\n-----Weight Converter-----")
        print("1. Pound to Kilogram.")
        print("2. Kilogram to Pound.")
        print("3. Gram to Kilogram.")
        print("4. Kilogram to Gram.")
        print("5. Pound to Gram.")
        print("6. Gram to Pound.")
        print("7. Exit")
        
        user_choice = input("Enter Your Choice: ").strip()

        if user_choice == "1":
            pound = get_user_input("Enter Weight in pounds: ")
            kg = pound / 2.20462
            print(f"\n{pound} pounds is equal to {kg:.2f} kilograms.")
        elif user_choice == "2":
            kg = get_user_input("Enter Weight in kilograms: ")
            pound = kg * 2.20462
            print(f"\n{kg} kilograms is equal to {pound:.2f} pounds.")
        elif user_choice == "3":
            gm = get_user_input("Enter Weight in grams: ")
            kg = gm / 1000
            print(f"\n{gm} grams is equal to {kg:.2f} kilograms.")
        elif user_choice == "4":
            kg = get_user_input("Enter Weight in kilograms: ")
            gm = kg * 1000
            print(f"\n{kg} kilograms is equal to {gm:.2f} grams.")
        elif user_choice == "5":
            pound = get_user_input("Enter Weight in pounds: ")
            gm = (pound / 2.20462) * 1000
            print(f"\n{pound} pounds is equal to {gm:.2f} grams.")
        elif user_choice == "6":
            gm = get_user_input("Enter Weight in grams: ")
            pound = (gm / 1000) * 2.20462
            print(f"\n{gm} grams is equal to {pound:.2f} pounds.")
        elif user_choice == "7":
            print("\nThank you.")
            break
        else:
            print("Invalid input! Please select an option between 1 and 7.")

if __name__ == "__main__":
    weight_converter()
