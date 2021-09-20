"""1.Create 5 file (.txt) and write messages in 
them."""
# first = open("first_names.txt", "w")
# first = first.write("This file contains first names of customers")
# second = open("second_name.txt", "w")
# second = second.write("This file contains second names of customers")
# dknow = open("gmails.txt", "w")
# dknow = dknow.write("This file contains customers's gmails")
# ends = open("age_and_gender.txt", "w")
# ends = ends.write("this file contains age and gender of customers")
# hihi = open("first_word.txt", "w")
# hihi = hihi.write("This file contains the preliminary agreements between customers and us")

"""2. Write a Python program to read first n lines of
a file."""
# d = open("first_names.txt","r")
# print(d.readline())
"""3.Write a Python program to append text to a file and
display the text."""
# c = open("second_name.txt","a")
# a = c.write("\nSome things can be added in this way")
# c.close()
# a = open("second_name.txt","r")
# print(a.readlines())
"""4.Write a python program to find the longest words."""
# k = []
# word = {"longest word":""}
# for i in a.readlines():
# 	for j in i.split():
# 		if len(j)>len(k):
# 			k = j
# 			word["longest word"] = k
# print(word)

"""5.Write a python program to find numbers in txt."""
# d = []
# for i in a.readlines():
# 	for j in i.split():
# 		for number in j:
# 			try:
# 				number = int(number)
# 				d.append(number)
# 			except ValueError:
# 				continue
# print(d)

"""6.Write a python program to get login and password."""
# log = input("write your log in: ")
# password =input("write your password: ")
# user = open("log_and_pass.txt","w")
# user = open("log_and_pass.txt","a")
# user.write(log + " " +password)
# user = open("log_and_pass.txt","r")
# print(user.readlines())

