class RecipeManagement:
    '''A class to manage individual recipes, including creating and updating recipe details.'''
    
    id_counter = 0

    def __init__(self, name, type, description):
        
        RecipeManagement.id_counter += 1
        self.id = RecipeManagement.id_counter
        self.name = name
        self.type = type
        self.description = description
                            
    @classmethod      
    def add_recipe(cls, recipes):
        name = input("\nEnter the name of the recipe: ")
        type = input("Enter the type of the recipe: ")
        description = input("Enter the description of the recipe: ")

        if not name or not type or not description:
            print("\nAll fields are required!")
        else:
            recipes.append(RecipeManagement(name, type, description))
            print("\nRecipe added successfully.")
            
    @classmethod    
    def update_recipe(cls, recipes):
        try:
            id = int(input("\nEnter the ID of the recipe to update: "))
            recipe = find_recipe_by_id(recipes, id)

            if recipe:
                name = input(f"\nEnter updated name (current: {recipe.name}) or press Enter to keep current: ")
                type = input(f"Enter updated type (current: {recipe.type}) or press Enter to keep current: ")
                description = input(f"Enter updated description (current: {recipe.description}) or press Enter to keep current: ")
                
                if name:
                    recipe.name = name
                if type:
                    recipe.type = type
                if description:
                    recipe.description = description
                print("\nRecipe updated successfully.")
            else:
                print("\nRecipe with the given ID not found.")
        except ValueError:
            print("\nInvalid ID. Please enter a number.")
            
    @classmethod       
    def delete_recipe(cls, recipes):
        try:
            id = int(input("\nEnter the ID of the recipe to delete: "))
            recipe = find_recipe_by_id(recipes, id)

            if recipe:
                confirm = input(f"\nAre you sure you want to delete recipe '{recipe.name}'? (y/n): ").lower()
                if confirm == "y":
                    recipes.remove(recipe)
                    print("\nRecipe deleted successfully.")
                else:
                    print("\nDeletion canceled.")
            else:
                print("\nRecipe with the given ID not found.")
        except ValueError:
            print("\nInvalid ID. Please enter a number.")
            
    @classmethod
    def display_recipe(cls, recipes):
        view_choice = input("\n1. View all recipes\n2. View a particular recipe\n> ")
        if view_choice == "1":
            if recipes:
                print("\n------- Recipe List -------")
                for recipe in recipes:
                    print(f"ID: {recipe.id}\nName: {recipe.name}\nType: {recipe.type}\nDescription: {recipe.description}")
                    print("--------------------------")
            else:
                print("\nNo recipes available.")
        elif view_choice == "2":
            try:
                id = int(input("\nEnter the ID of the recipe to view: "))
                recipe = find_recipe_by_id(recipes, id)

                if recipe:
                    print("\n------- Recipe -------")
                    print(f"ID: {recipe.id}\nName: {recipe.name}\nType: {recipe.type}\nDescription: {recipe.description}")
                else:
                    print("\nRecipe with the given ID not found.")
            except ValueError:
                print("\nInvalid ID. Please enter a number.")
        else:
            print("\nInvalid choice!")
            

def find_recipe_by_id(recipes, id):
    '''Finds a recipe in the list of recipes by its unique ID.'''
    for recipe in recipes:
        if recipe.id == id:
            return recipe
    return None


def main():
    '''The Main function for the Recipe Management system.'''
    recipes = []

    while True:
        try:
            print("\n------ Recipe Management ------")
            print("1: Add Recipe")
            print("2: Update Recipe")
            print("3: Delete Recipe")
            print("4: View Recipes")
            print("5: Exit")
            choice = input("Enter Your Choice: ")

            if choice == "1":
                RecipeManagement.add_recipe(recipes)

            elif choice == "2":
                RecipeManagement.update_recipe(recipes)

            elif choice == "3":
                RecipeManagement.delete_recipe(recipes)

            elif choice == "4":
                RecipeManagement.display_recipe(recipes)

            elif choice == "5":
                print("\nExiting Recipe Management. Thank You!")
                break

            else:
                print("\nInvalid choice! Please enter a number between 1 and 5.")

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
