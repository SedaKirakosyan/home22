"""1. century"""
# class century:
# 	def __init__(self,year):
# 		self.year = year
# 	def result(self):
# 		year = self.year
# 		if year % 100 == 0:
# 			return year // 100
# 		else:
# 			return year // 100 +1
# res = century(2001)
# print(res.result())

"""2. Palindrome"""
# class palindrome:
# 	def __init__(self,word):
# 		self.word = word
# 	def test(self):
# 		word = self.word
# 		if word[:] == word[::-1]:
# 			return "The word is palindrome"
# 		else:
# 			return "The word isn't palindrome"
# w = palindrome("abba")
# print(w.test())

"""3. Largest
Create a Class which given an list of integers, find the pair 
of adjacent elements that has the largest product and 
return that product."""
# class largest:
# 	def __init__(self,lis):
# 		self.lis = lis
# 	def pair(self):
# 		lis = self.lis
# 		new = []
# 		for i in range(len(lis)-1):
# 			new.append(lis[i]*lis[i+1])
# 		return max(new)
# mylist =  largest([3, 6, -2, -5, 7, 3])
# print(mylist.pair())

"""4. find highest word
Create a class which given a list of strings, return another list 
containing all of its longest strings."""
# class highest:
# 	def __init__(self,lis):
# 		self.lis = lis
# 	def test(self):
# 		lis = self.lis
# 		l = []
# 		for i in lis:
# 			l.append(len(i))
# 		c = max(l)
# 		new =[]
# 		for j in lis:
# 			if len(j) == c and j not in new: #mi qich avelacrel em pahanjy
# 				new.append(j)
# 		return new 
# List = highest(["aba", "aa", "ad", "vcd", "aba"])
# print(List.test())    

"""5. Lucky
Ticket numbers usually consist of an even number of digits.A ticket number is 
considered lucky if the sum of the first half of the digits is equal to the sum of the 
second half.Given a ticket number n, determine if it's lucky or not."""
# class lucky:
# 	def __init__(self,ticket):
# 		self.ticket = ticket
# 	def number(self):
# 		ticket = str(self.ticket)
# 		a = []
# 		b = []
# 		a.append(int(ticket[0:len(ticket)//2]))  
# 		b.append(int( ticket[len(ticket)//2:]))
# 		if sum(a) == sum(b):
# 			return "Lucky"
# 		else:
# 			return "Unlucky"
# n = lucky(124124)
# print(n.number())

"""6. List sort
Create a class: Some people are standing in a row in a park. There are trees 
between them which cannot be moved. Your task is to rearrange the people by 
their heights in a non-descending order without moving the trees. People can be 
very tall!"""
# class park:
# 	def __init__(self,plis):
# 		self.plis = plis
# 	def moving(self):
# 		plis = self.plis
# 		ones = []
# 		other = []
# 		for i in range(len(plis)):
# 			if plis[i] == -1:
# 				ones.append(i)
# 			else:
# 				other.append(plis[i])
# 		other = sorted(other)
# 		for j in ones:
# 			other.insert(j,plis[j])
# 		return other
# a = park([-1, 150, 190, 170, -1, -1, 160, 180])
# print(a.moving())

"""7. Weight"""
# class people:
# 	def __init__(self,list_):
# 		self.list_ = list_
# 	def test(self):
# 		list_ = self.list_
# 		return [sum(list_[::2]),sum(list_[1::2])]
# example = people( [50, 60, 60, 45, 70])
# print(example.test())
