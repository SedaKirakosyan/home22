"""Task1"""
# import math
# class covid:
# 	def __init__(self,temp):
# 		self.temp = temp
# 	def res(self):
# 		temp = self.temp
# 		d = temp*math.pi
# 		if 128<=math.ceil(d) <= 120 :
# 			print("Everything is ok")
# 		else:
# 			print("You have coronavirus")
# a = covid(38.1)
# a.res()

"""Task2"""
# import  string
# class name:
# 	def __init__(self,n):
# 		self.n = n
# 	def g(self):
# 		let = string.ascii_lowercase
# 		di = {}
# 		for i in range(1,10):
# 			di[i] = (let[i-1::9])
# 		n = (self.n).lower()
# 		c = 0
# 		d = 0
# 		for i in di.values():
# 			for j in i:
# 				if c==len(n):
# 					pass
# 				elif n[c] == j:
# 					c += 1
# 					d += list(di.keys())[list(di.values()).index(i)]
# 					print(j,c)
# 					if c == len(n):
# 								pass
# 				else:
# 					for i in di.values():
# 						for j in i:
# 							if c == len(n):
# 								pass
# 							else:
# 								if n[c] == j:
# 									c += 1
# 									d += list(di.keys())[list(di.values()).index(i)]
# 									print(j,c)
# 		if d ** 0.5 <5:
# 			return d, "Yes"
# 		else:
# 			return d, "No"
# res = name("kim") #Shakirayi depqum xndri tvyallnery sxal en
# print(res.g())

"""Task3"""
import random
class Harry:
	def __init__(self,f,s,t):
		self.f = f
		self.s = s
		self.t = t 
	def ch(self):
		f = self.f 
		s = self.s 
		t = self.t
		sample = [f,s,t]
		point = 0
		for i in range(3):
			c= random.choice(sample)
			if c == sample[i]:
				point += 1
				print(c,point)
			else:
				point -= 1
				print(c,point)
		if point >= 2:
			return "You win"
		else: 
			return "You lose"	
res = Harry("Avada Kedavra","Crucio","Imperio")
print(res.ch())


