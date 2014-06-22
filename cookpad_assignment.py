# coding: utf-8

def display_recipes_with_id(recipes):
	Id = 0
	for recipe in recipes:
		print( Id, recipe.rstrip() )
		Id += 1

def display_target_recipe(recipes, Id):
	Id = int(Id)
	print( Id, recipes[Id].rstrip() )

if __name__ == "__main__":
	file_name = input( "input file_name > " )
	recipes   = open( file_name, "r" ).readlines()

	uniq_id = input("input recipe id (0, 1, ...) > ")
	if(uniq_id == ""):
		display_recipes_with_id(recipes)
	else:
		display_target_recipe(recipes, uniq_id)
