ingredient_one = input("Enter ingredient 1: ")
ounces_of_one = float(input(f"Ounces of {ingredient_one}: "))
ingredient_two = input("Enter ingredient 2: ")
ounces_of_two = float(input(f"Ounces of {ingredient_two}: "))
ingredient_three = input("Enter ingredient 3: ")
ounces_of_three = float(input(f"Ounces of {ingredient_three}: "))
servings = float(input("Number of servings: "))

total_ounces_one = servings*ounces_of_one 
print(f"Total ounces of {ingredient_one}: {total_ounces_one}")
total_ounces_two = servings*ounces_of_two
print(f"Total ounces of {ingredient_two}: {total_ounces_two}")
total_ounces_three = servings*ounces_of_three
print(f"Total ounces of {ingredient_three}: {total_ounces_three}")            
