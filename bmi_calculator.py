def BMI_calculator(weight, height):
    """Calculate BMI and return the corresponding category."""
    
    bmi_score= weight / ((height/100)**2)
    
    if bmi_score<18.5:
        return bmi_score,"Underweight"
    elif bmi_score>=18.5 and bmi_score<25:
        return bmi_score,"Normal"
    elif bmi_score>=25 and bmi_score<30:
        return bmi_score,"Overweight"
    elif bmi_score>=30:
        return bmi_score,"Obesity"     

def get_valid_input(prompt, value_type=float):
    """for user input and validate it."""
    
    while True:
        user_input=input(prompt).strip()
        try:
            value=value_type(user_input)
            
            if value_type!=str:
                if value<=0:
                    print(">>Value should be greater than 0.\n")
                else:
                    return value
            else:
                if not all(c.isalpha() or c.isspace() for c in user_input.strip()) or len(user_input.strip()) == 0:
                    print(">> Name should only contain alphabetic characters and spaces, and cannot be empty.\n")
                else:
                    return value
            
        except ValueError:
            print(f">>Invalid input. please enter numeric value")
    

def main():
    """Main function to calculate and display BMI."""
    
    print("------BMI Calculator------")
    print("Fill up the following details:")
    
    name=get_valid_input("\nEnter Your Name: ",str) 
    height=get_valid_input("\nEnter Your Height(in cm): ")
    weight=get_valid_input("\nEnter Your Weight(in kg): ")

    bmi_value, category = BMI_calculator(weight, height)
    
    print(f"\n{name.title()}, your BMI is {bmi_value:.2f}, which falls under the '{category}' category.")

        

if __name__=="__main__":
    main()