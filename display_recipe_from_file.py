#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_recipe_from_file():
	recipe_file = open('recipe-data.txt')
	print(recipe_file.read(), end="")
	recipe_file.close()

if __name__ == "__main__":
	read_recipe_from_file()

