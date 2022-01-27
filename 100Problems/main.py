# Question 1

# print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")

# Question 2

# n = int(input())

# fact = 1
# i = 1
# while i <= n:
#   fact = fact * i
#   i += 1
# print(fact)

# Question 3

# n = int(input())

# dict = {}
# i = 1

# while i <= n:
#   dict[i] = i**2
#   i += 1

# print(dict)

# Question 4

# my_list = input().split(',')

# my_tuple = tuple(my_list)

# print(my_list)
# print(my_tuple)

# Question 5

# class UserIO:
#   def __init__(self):
#     pass
  
#   def get_string(self):
#     self.str = input()

#   def print_string(self):
#     print(self.str.upper())

# a = UserIO()
# a.get_string()
# a.print_string()

# Question 6

# from math import *  # importing all math functions

# C, H = 50, 30

# def calc(D):
#     D = int(D)
#     return str(int(sqrt((2 * C * D) / H)))

# D = input().split(",")
# D = list(map(calc, D))  # applying calc function on D and storing as a list
# print(",".join(D))

# Question 7

