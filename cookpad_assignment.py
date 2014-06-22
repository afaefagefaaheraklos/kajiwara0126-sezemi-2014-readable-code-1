
	
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
	spec = input("select the spec you want to use > ")
	spec = int(spec)	# inputの型を数値型に変換
	if   spec == 1:
		display_recipe()
	elif spec == 3:
		display_recipe_from_file()
	elif spec == 4:
		display_recipes_from_file()
	else:
		pass
	
	
