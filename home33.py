"""1.Write a python class to find max, min num and 
and sum in your list:
don’t use max sum and min function"""
# class maxmin:
# 	def __init__(self,mylist):
# 		self.mylist = mylist
# 	def res(self):
# 		mylist = self.mylist
# 		c = mylist[0]
# 		b = 0
# 		d = mylist[0]
# 		for i in range(len(mylist)):
# 			if mylist[i] >= c:
# 				c = mylist[i]
# 			elif mylist[i] <= d:
# 				d = mylist[i]
# 			b += mylist[i]
# 		return b,c,d
# a = maxmin([4,2,3,6,10])
# print(a.res())

"""2.Write a python class to find two highest values in 
your dict:"""
# class value:
# 	def __init__(self,mydict):
# 		self.mydict = mydict
# 	def search(self):
# 		mydict = self.mydict
# 		res = sorted(mydict.values())
# 		return res[-2:]
# res = value({"a":4,"b":10,"c":25,"d":3})
# print(res.search())

"""3.Write a python class where your child class takes 
all methods in parent class and print them."""
# class Parent:
# 	def __init__(self,name,age,mail):
# 		self.name = name
# 		self.age = age
# 		self.mail = mail
# class baby(Parent):
# 	def __init__(self,name,age,mail):
# 		super().__init__(name,age,mail)
# 	def theend(self):
# 		return self.name,self.age,self.mail

# res = baby("Bob",22,"******.@gmail.com")
# print(res.theend())

"""4.Write a Python class named Rectangle
constructed by a length and width and a method
which will compute the area of a rectangle."""
# class rectangle:
# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width
# 	def area(self):
# 		length = self.length
# 		width = self.width
# 		return length * width
# example = rectangle(10,11)
# print(example.area())

"""5.Write a python class where we use polymorphism"""
# class table:
# 	def color(self):
# 		return "Blue"
# class chair:
# 	def color(self):
# 		return "Black"
# a = table()
# b = chair()
# print(a.color())
# print(b.color())
























