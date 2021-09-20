"""1. Write a Python program to add info in JSON file
about you."""
# import json
# name = input("Write your name: ")
# age = int(input("Write your age: "))
# color = input("What is your favorite color: ")
# info = {"name":name,
# 		"age":age,
# 		"color":color
# }
# file = open("information.json","w")
# json.dump(info,file)
# file = open("information.json","r")
# print(json.load(file))

"""2. Write a Python program to get info in JSON file
about you."""
import json
file = open("information.json","r")
# print(json.load(file))

"""3. Write a Python program to check if your json file
have this info."""
my_list = ['Seda',"245",'black']
try:
	my_list in file
	print("Everything is ok!")
except:
	print("You have isymmetry!")



