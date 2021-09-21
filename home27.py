"""1. Dict
You have two list convert it in dictionary and add 
in (mydict.txt) and show result"""
# first = ["a","b","c"]
# second = [4,5,8]
# my_dict = {i:j for i,j in zip(first,second)}
# file = open("dict.txt","w")
# file.write(str(my_dict))
# file = open("dict.txt","r")
# file.close()

"""2. Json
Create json file and save them lyrics (song) 
and print in cmd word this song."""
# import json
# song = open("lyrics.json","w")
# lyrics = input("Write lyrics: ")
# json.dump(lyrics,song)
# song.close()
# song = open("lyrics.json","r")
# print(json.load(song))
# song.close()

"""3. Function
Write a python program which have one input an 
integer, representing the sum of all the multiples of 
3 and 5 below the given input. and save this result 
in json file."""
# import json
# number = int(input("number: "))
# mul = open("mul.json","w")
# sums = 0
# for i in range(1,number+1):
# 	if i % 3 == 0 and i % 5 == 0:
# 		sums += i	
# json.dump(sums,mul)
# mul.close()
# mul = open("mul.json","r")
# print(json.load(mul))
# mul.close()

"""4. Vowels
Write a program that takes in a string as input, 
counts and outputs the number of vowels. 
And add result in json file."""
# import json
# word = input("Say something: ").lower()
# vowels = 0
# for i in word:
# 	if 	(i == "a" or i == "e" or
# 		i == "i"
# 		or i == "o" or i == "u"
# 		):
# 		vowels += 1
# # print(vowels)
# count = open("count.json","w")
# json.dump(vowels,count)
# count.close()
# count = open("count.json","r")
# print("The numbers of vowels: " + str(json.load(count)))
# count.close()

"""5. text
Create dict """
# file = open("words.txt","w")
# file.write("Another pause and more eying and siding around each other")
# file.close()
# file = open("words.txt","r")
# file = file.readline().split()
# dict_ = {}
# for i in file: 
# 	dict_[i] = file.count(i)
# print(dict_)
# file.close()

"""6. NEw list
Write a python function which get a new list 
from a given list, consisting of the first 
repeating elements."""
# my_list = ["a","b","c","a","b"]
# new_list = list(set(my_list))
# print(new_list)

"""7. How much 
You have word.txt file and in them you have 
one story.
Write a Python function that accepts this 
story and calculate the number of uppercase 
letters and lowercase letters."""
# text = open("lowercase.txt","r")
# lowc = 0
# upc = 0
# for i in str(text.readlines()):
# 	print(i)
# 	if i.isalpha() == False:
# 		continue 
# 	elif i.islower():
# 		lowc += 1
# 	else:
# 		upc += 1
# print(f'Lowercases: {lowc} \nUppercases: {upc}')
# text.close()

"""8. test
You have test.txt file and in them you have 
one story overwrite this story in another file."""
# file1 = open("lowercase.txt","r")
# file2 = open("lowec.txt","a")
# file2.write(file1.read())
# file2 = open("lowec.txt","r")
# print(file2.readlines())
# file1.close()
# file2.close()

















