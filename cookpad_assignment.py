# coding: utf-8

if __name__ == "__main__":
	file_name = input("input the file_name, you want to use > ")
	selected_recipe = open(file_name, "r")

	recipes = selected_recipe.readlines()
	uniq_id = 1
	
	for recipe in recipes:
		print( uniq_id, recipe.rstrip() )
		uniq_id += 1
