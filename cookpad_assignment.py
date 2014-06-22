def display_recipe():
	print("ome-rice")

def display_recipe_from_file():
	recipe_name = open('recipe-data.txt')
	print(recipe_name.read(), end="")
	recipe_name.close()

def display_recipes_from_file():
	recipes_name = open('recipes-data.txt')
	print(recipes_name.read(), end="")
	recipes_name.close()

if __name__ == "__main__":
	file_name = input("input the file_name, you want to use > ")
	selected_recipe = open(file_name, "r")

	recipe = selected_recipe.read()
	print( recipe )
