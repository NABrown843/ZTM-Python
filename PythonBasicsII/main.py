# Conditional Logic

# is_old = True
# is_licensed = True

# if is_old and is_licensed:
#   print('You are old enough to drive and you have a license!') # if is_old is True
# else:
#   print('You are not of age') # new line

# print('okoko')

# Truthy vs Falsey

# is_old = True
# is_licensed = True

# print(bool('hello'))
# print(bool(5))

# print(bool(''))
# print(bool(0))

# password = '123'
# username = 'Johnny'

# if password and username:
#   print('you have entered a username and password')
# else:
#   print('Please enter username and password')

# Ternary Operator

# condition_if_true if condition else condition_if_else

# is_friend = False
# can_message = 'message allowed' if is_friend else 'messaging not allowed'
# print(can_message)

# Short Circuiting

# is_friend = True
# is_user = True

# if is_friend or is_user:
#   print('best friends forever')

# Logical Operators

# print(4 > 5)
# print(4 == 5)
# print('a' > 'b') # compares unicode ord('a')
# print(4 >= 4)
# print(0 != 0)
# print(not(1 == 1))

# Exercise: Logical Operators

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
#   print('You are a master magician')
# elif is_magician and not is_expert:
#   print('At least you\'re getting there')
# elif not is_magician:
#   print('You need magic powers')

# # is vs ==
# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

# For Loops

# for item in 'Zero to Mastery':
#   print(item)

# for item in [1,2,3]:
#   print(item)
#   print(item)

# for item in (1,2,3,4,5):
#   for x in ['a','b','c']:
#     print(item, x)

# Iterables
# can be list, dictionary, tuple, string, set
# can be iterated over -> one by one check each item in the collection

# user = {
#   'name': 'Golem',
#   'age': 5006,
#   'can_swim': False
# }

# for item in user:
#   print(item)

# for item in user.items():
#   print(item)

# for item in user.values():
#   print(item)

# for item in user.keys():
#   print(item)

# for key, value in user.items():
#   print(key, value)

# Exercise: Tricky Counter

# my_list = [1,2,3,4,5,6,7,8,9,10]
# counter = 0

# for item in my_list:
#   counter += item

# print(counter)

# range()

# print(range(100))

# for number in range(100):
#   print(number)

# for _ in range(0,10,2):
#   print(_)

# for _ in range(10,0,-2):
#   print(_)

# enumerate()

# for i,char in enumerate('hello'):
#   print(i,char)

# for i,number in enumerate((1,2,3)):
#   print(i,number)

# for i,char in enumerate(list(range(100))):
#   if char == 50:
#     print(f'index of 50 is: {i}')

# while loops

# i = 0
# while i < 50:
#   print(i)
#   i += 1
# else:
#   print('done with all the work')

# while loops 2

# my_list = [1,2,3]
# for item in my_list:
#   print(item)

# i = 0
# while i < len(my_list):
#   print(my_list[i])
#   i += 1

# while True:
#   response = input('say something: ')
#   if (response == 'bye'):
#     break

# Our First GUI

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# iterate over picture
#   if 0 -> ' '
#   if 1 -> print *

# image = 0
# while image < len(picture):
#   pixel = 0
#   while pixel < len(picture[image]):
#     if picture[image][pixel] == 0:
#       print(' ', end = '')
#     elif picture[image][pixel] == 1:
#       print('*', end = '')
#     pixel += 1
#   image += 1
#   print('')

# for image in picture:
#   for pixel in image:
#     if pixel == 1:
#       print('*', end = '')
#     else:
#       print(' ', end = '')
#   print('')

# Developer Fundamentals IV

# clean
# Readability
# predictability
# DRY (Do Not Repeat Yourself)

# Exercise: Find Duplicates

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# some_list.sort()

# i = 1
# while i < len(some_list):
#   if some_list[i] == some_list[i - 1]:
#     print(some_list[i])
#   i += 1

# duplicates = []
# for value in some_list:
#   if some_list.count(value) > 1:
#     if value not in duplicates:
#       duplicates.append(value)

# print(duplicates)

# Functions
# DRY
# def say_hello():
#   print('hellllooooo')

# say_hello()

# def show_tree():
#   for image in picture:
#     for pixel in image:
#       if pixel == 1:
#         print('*', end = '')
#       else:
#         print(' ', end = '')
#     print('')

# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# show_tree()
# show_tree()
# show_tree()

# Parameters and Arguments

# parameters
# def say_hello(name, emoji):
#   print(f'hellllooooo {name} {emoji}')

# arguments
# say_hello('Bob', ':P') #call/invoke function
# say_hello('John', ':P') #call/invoke function
# say_hello('Sarah', ':P') #call/invoke function

# Default Parameters and Keyword Arguments

# positional arguments
# say_hello('Bob', ':P') #call/invoke function
# say_hello('John', ':P') #call/invoke function
# say_hello('Sarah', ':P') #call/invoke function

# keyword arguments
# say_hello(emoji = ':P', name = 'Bob') #call/invoke function
# say_hello(emoji = ':P', name = 'John') #call/invoke function
# say_hello(emoji = ':P', name = 'Sarah') #call/invoke function

# default parameters
# def say_hello(name = 'Darth Vader', emoji = '>:('):
#   print(f'hellllooooo {name} {emoji}')

# say_hello()
# say_hello('Bob', ':P')