# coding: utf-8

if __name__ == "__main__":
	file_name = input("input the file_name, you want to use > ")
	selected_recipe = open(file_name, "r")

	recipe = selected_recipe.read()
	print( recipe )
