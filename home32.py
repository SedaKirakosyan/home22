"""1.Calculator"""
# class calculator:
#     def __init__(self,first,sign,second):
#         self.first = first
#         self.sign = sign
#         self.second = second
#     def f(self):
#         first = self.first
#         sign = self.sign
#         second = self.second
#         if sign == "+":
#                 return first + second
#         elif sign == "-":
#                 return first - second
#         elif sign == "*":
#                 return first * second
#         else:
#             if second == 0:
#                 print("Can't divide by zero")           
#             else:
#                 return first / second 
# basic = calculator(4,"/",0)
# print(basic.f())

"""2.Create a class for Car and Person"""
# class Person: 
#     def __init__(self, name,car):
#         self.name = name  
#         self.car = car
#     def f(self):  
#         print("i'm " + self.name + " i've a " + self.car)
# p1 = Person("Jon","Tucson")
# p1.f()

"""3. Create a class Change:You have 3 methods 
in your class:
Usd --- Eur
Usd --- Amd
Usd --- Ru"""
# class exchang:
#     def __init__(self,usd,other):
#         self.usd = usd
#         self.other = other
#     def change(self):
#         a = {"eur":0.862,"amd":482.5,"ru":71.4}
#         if self.other in a:
#             return self.usd * a[self.other]
#         else:
#             return "Something went wrong"
# res = exchang(1000,"ru")
# print(res.change())










