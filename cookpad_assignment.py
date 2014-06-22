
	
def display_recipe():
	print("ome-rice")

def display_reccipe_from_file():
	recipe_name = open('recipe-data.txt')
	print(recipe_name.read, end="")
	recipe_name.close()

if __name__ == "__main__":
	spec = input("select the spec you want to use > ")
	if spec == 1:
		display_recipe()
	elif spec == 3:
		diplay_recipe_from_file()
	else:
		pass
	
	
