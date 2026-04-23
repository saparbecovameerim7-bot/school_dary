# from django.test import TestCase

# Create your tests here.


# def date(day, month, year):
#   events_list = [[1, 5, 2026],  [5, 5, 2026],[31, 8, 2026]]
#   for i in events_list:
#     if day in i and month in i and year in i:
#       return True
#     else:
#       return "Такого ивента нет"
    
# print(date(1, 5, 2026))

#Tuple - кортеж

# email = ("alexgmail.com", "tomgmail.com")
# email2 = ["alexgmail", "tomgmail.com"]

# new_email1 = tuple(email1)

# email1, email = new_email1
# num1, num2 = 1, 2  

# print(new_email1)

# tom = ("tom", 37, "Google", "software developer")

# copy_tom = tom[1, 3]
# print(copy_tom)

# def get_user():
#   name = "User"
#   age = 18 
#   company ="Meta"
#   return name, age, company

# print(get_user())

# tom = get_user()

# if 18 in tom:
#   print("Your an adult")
# else:
#   print("Your a child")
  

# name1 = "alex"

# def say_hi(): 
#   name2 = "tom"
#   print(f"local: {name2} ")
# say_hi()
# print(f"global: {name1}") 

# def outer():
#   n = 5
#   def inner():
#     nonlocal n
#     n = 25 
#     print(n)
    
#   inner()
#   print(n) 

# outer()
    
# closure - замыканаие

# def outer():
#   likes = 0 
  
#   def inner():
#     nonlocal likes
#     likes += 1 
#     print(likes) 

#   return inner

# fn = outer()
# fn()
# fn()
# fn() 

def multiply(n):
  def inner(m): return n * m
  return inner 
fn = multiply(2)
print(fn(3))