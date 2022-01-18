# Data Types
# int and float
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))
# print(type(5.00001))
# print(type(0))
# print(type(9.9 + 1.1))

# print(2**2) #Exponent

# print(2 // 4) #Floor

# print(5 % 4) #Modulo (remainder)

# math functions
# print(round(3.9))
# print(abs(-20))

# operator precedence
# print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

# Exercise # 1
# print((5 + 4) * 10 / 2) # 45.0

# print(((5 + 4) * 10) / 2) # 45.0

# print((5 + 4) * (10 / 2)) # 45.0

# print(5 + (4 * 10) / 2) # 25.0

# print(5 + 4 * 10 // 2) # 25

# complex # another data type

# binary
# print(bin(5))
# print(int('0b101', 2))

# variables
# iq = 190
# print(iq)

# snake_case
# start with lowercase or underscore
# letters, numbers, underscores
# case sensitive
# don't overwrite keywords

# iq = 190
# user_age = iq / 4
# a = user_age
# print(a)

# # constants
# PI = 3.14

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# Statements and Expressions
# iq = 100
# user_age = iq / 5

# augmented assignment operator
# some_value = 5
# some_value = some_value + 2
# some_value += 2
# some_value -= 2
# print(some_value)

# Exercise 2

# counter = 0

# counter += 1
# counter += 1
# counter += 1
# counter += 1
# counter -= 1
# counter *=2

# #Before you click RUN, guess what the counter variable holds in memory!
# print(counter) # 6

# Strings
# 'hi hello there!'
# "hi hello there!"
# print(type("hi hello there!"))

# username = 'supercoder'
# password = 'supersecret'

# long_string = '''
# WOW
# 0 0
# ---
# '''

# print(long_string)

# first_name = 'John'
# last_name = 'Smith'
# full_name = first_name + ' ' + last_name
# print(full_name)

# string concatenaion
# print('hello' + ' John')
# print('hello' + 5) # TypeError

# Type conversion
# print(type(int(str(100))))

# Escape Sequences
# weather = '\t It\'s \"kind of\" sunny \n hope you have a good day!'
# print(weather)

# Formatted Strings
# name = 'Johnny'
# age = 55
# print('hi ' + name + '. You are ' + str(age) + ' years old')
# print(f'hi {name}. You are {age} years old')
# print('hi {}. You are {} years old'.format(name, age))
# print('hi {1}. You are {0} years old'.format(name, age))
# print('hi {new_name}. You are {age} years old'.format(new_name = 'sally', age = 100))

# Exercise # 3
# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

# print("Hello {}, your balance is {}.".format("Cindy", 50)) # Hello Cindy, your balance is 50.

# print("Hello {0}, your balance is {1}.".format("Cindy", 50)) # Hello Cindy, your balance is 50.

# print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50)) # Hello Cindy, your balance is 50.

# print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50)) # Hello Cindy, your balance is 50.

# # 2 How would you write this using f-string? (Scroll down for answer)

# name = 'Cindy'
# amount = 50

# print(f'Hello {name}, your balance is {amount}.')

# string indexes

# selfish = 'me me me'
# print(selfish[0])
# print(selfish[7])
# print(selfish)

# selfish = '01234567'
# # [start:stop]
# print(selfish[0:2])
# print(selfish[0:7])
# print(selfish[0:8])

# # [start:stop:stepover]
# print(selfish[0:8:2])

# print(selfish[1:])
# print(selfish[:5])
# print(selfish[::1])
# print(selfish[::-1])

# Exercise 4
#Guess the output of each print statement before you click RUN!
# python = 'I am PYHTON'

# print(python[1:4]) # ' am'
# print(python[1:]) # ' am PYHTON'
# print(python[:]) # 'I am PYHTON'
# print(python[1:100]) # ' am PYHTON'
# print(python[-1]) # 'N'
# print(python[-4]) # 'H'
# print(python[:-3]) # 'I am PYH'
# print(python[-3:]) # 'TON'
# print(python[::-1]) # 'NOTHYP ma I'

# Immutability
# selfish = '01234567'
# selfish = 100
# print(selfish)
# selfish = '01234567'
# selfish[0] = '8' # TypeError. Can't reassign part of a string

# Built-In Functions + Methods
# greet = 'hellloooo'
# print(greet[0:len(greet)])

# quote = 'to be or not to be'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.find('be'))
# print(quote.replace('be','me'))
# print(quote)
# quote2 = quote.replace('be','me')
# print(quote2)

# Booleans
# bool True or False
# name = 'John'
# is_cool = False
# is_cool = True

# print(bool(1))
# print(bool(0))

# Exercise 5: Type Conversion
# name = 'John Smith'
# age = 50
# relationship_status = 'engaged'
# relationship_status = 'married'

# from datetime import date

# birth_year = input('What year were you born? ')
# age = date.today().year - int(birth_year)
# print(f'Your age is {age}.')

# Exercise: Password Checker

# username = input('Enter your username: ')
# password = input('Enter your password: ')

# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'{username}, your password {hidden_password} is {password_length} characters long')

# Lists

# li = [1,2,3,4,5]
# li2 = ['a','b','b']
# li3 = [1, 2.5, 'a', True]

# amazon_cart = ['notebooks', 'sunglasses']
# print(amazon_cart[0])

# lists are a form of array

# List Slicing

# amazon_cart = [
#   'notebooks', 
#   'sunglasses',
#   'toys',
#   'grapes'
#   ]
# amazon_cart[0] = 'laptop'
# print(amazon_cart[0:3])

# new_cart = amazon_cart # becomes pointer
# new_cart = amazon_cart[:] # becomes new list

# lists Exercise

#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
# new_list = ['a', 'b', 'c']
# print(new_list[1]) # b
# print(new_list[-2]) # b
# print(new_list[1:3]) # b,c
# new_list[0] = 'z'
# print(new_list) # z,b,c

# my_list = [1,2,3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list) # z,2,3
# print(bonus) # 1,2,3,5

# Matrix

# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# print(matrix[0][1])

# Matrix Exercise

# # using this list: 
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# # access "Oranges" and print it:
# # You will find the answer if you scroll down to the bottom, but attempt it yourself first!
# print(basket[1][1][0])

# List Methods

# basket = [1,2,3,4,5]
# print(len(basket))

# # adding
# basket.append(100)
# new_list = basket
# print(new_list)

# basket.insert(4, 100)
# print(basket)

# basket.extend([100,101])
# print(basket)

# removing
# basket.pop()
# basket.pop(0)
# print(basket)

# basket.remove(4)
# print(basket)

# basket.clear()
# print(basket)

# List Methods 2

# basket = ['a','b','c','d','e']
# print(basket.index('d'))
# print(basket.index('d',0,4))
# print('d' in basket)
# print('x' in basket)

# print(basket.count('d'))

# List Methods 2 Exercise

# # using this list, 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# # 1. Remove the Banana from the list
# basket.pop(0)

# # # 2. Remove "Blueberries" from the list.
# basket.pop()

# # # 3. Put "Kiwi" at the end of the list.
# basket.append('Kiwi')

# # # 4. Add "Apples" at the beginning of the list
# basket.insert(0,'Apples')
# # # 5. Count how many apples in the basket
# print(basket.count('Apples'))
# # # 6. empty the basket
# basket.clear()

# print(basket)

# List Methods 3

# basket = ['x','a','b','c','d','e','d']
# # basket.sort() # sorts list
# print(sorted(basket)) # does not alter list
# print(basket)

# new_list = basket.copy()
# print(new_list)

# basket.reverse()
# print(basket)

# Common List Patterns

# basket = ['x','a','b','c','d','e','d']
# # basket.sort()
# # print(basket[::-1])

# # print(list(range(1,100)))
# # print(list(range(100)))

# sentence = ' '
# new_sentence = sentence.join(['hi','my','name','is','JOJO'])
# print(new_sentence)

# new_sentence = ' '.join(['hi','my','name','is','JOJO'])
# print(new_sentence)

# Common List Patterns Exercise

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
# friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

# new_friend = ['Stanley']

# friends.extend(new_friend)
# print(sorted(friends))

# friends.append(new_friend[0])
# friends.sort()
# print(friends)

# list unpacking

# a,b,c, *other,d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# None

# Null # Absence of value

# weapons = None
# print(weapons)

# Dictionary

# dict

# dictionary = {
#   'a' : 1,
#   'b' : 2,
#   'x' : 3
# }

# print(dictionary['b'])
# print(dictionary)

# dictionary2 = {
#   'a': [1,2,3],
#   'b': 'hello',
#   'x': True
# }

# print(dictionary2)

# my_list = [
#   {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
#   },
#   {
#     'a': [4,5,6],
#     'b': 'hello',
#     'x': True
#   }
# ]

# print(my_list[0]['a'][2])
# print(my_list[0]['a'][1])

# Dictionary Methods

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }
# print(user.get('age',55))

# user2 = dict(name='JohnJohn')
# print(user2)

# Dictionary Methods 2

# user = {
#   'basket': [1,2,3],
#   'greet': 'hello',
#   'age': 20
# }

# # print('hello' in user)
# # print('hello' in user.keys())
# # print('hello' in user.values())

# # user2 = user.copy()

# # print(user.clear())
# # print(user2)

# # user.pop('age')
# # print(user)

# # user.popitem()
# # print(user)

# user.update({'age': 55})
# print(user)

# user.update({'ages': 55})
# print(user)

# Dictionary Methods 2 Exercise

#Scroll down to see the answers!
#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

#2 iterate and print all the keys in the above user.

#3 Add a new weapon to your user

#4 Add a new key to include 'is_banned'. Set it to false

#5 Ban the user by setting the previous key to True

#6 create a new user2 my copying the previous user and update the age value and username value. 

# user = {
#   'age': 33,
#   'username': 'George Carlin',
#   'weapons': ['sword','knife','bow'],
#   'is_active': True,
#   'clan': None
# }

# print(user.keys())

# user['weapons'].append('arrow')
# print(user.get('weapons'))

# user.update({'is_banned': False})
# print(user)

# user.update({'is_banned': True})
# print(user)

# user2 = user.copy()
# user2.update({'age': 25, 'username': 'Patton Oswalt'})
# print(user2)

# Tuples
# Immutable Lists

# my_tuple = (1,2,3,4,5)
# print(my_tuple[2])
# print(5 in my_tuple)

# Tuples 2
# x,y,z, *other = (1,2,3,4,5)

# print(x)
# print(y)
# print(z)
# print(other)

# my_tuple = (1,2,3,4,5)
# print(my_tuple.count(5))
# print(my_tuple.index(5))
# print(len(my_tuple))

# Sets
# unordered collection of unique objects

# my_set = {1,2,3,4,5,5}
# print(my_set)

# my_set.add(100)
# my_set.add(2)
# print(my_set)

# my_list = [1,2,3,4,5]
# print(set(my_list))

# my_set = {1,2,3,4,5,5}

# print(1 in my_set)
# print(len(my_set))
# print(list(my_set))

# new_set = my_set.copy()
# my_set.clear()
# print(new_set)
# print(my_set)

# Sets 2

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# my_set.discard(5)
# print(my_set)

# my_set.difference_update(your_set)
# print(my_set)

# print(my_set.intersection(your_set))
# print(my_set & your_set)
# print(my_set.isdisjoint(your_set))

# print(my_set.union(your_set))
# print(my_set | your_set)

# my_set = {4,5}

# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))

# Sets Exercise

# # You are working for the school Principal. We have a database of school students:
# school = {'Bobby','Tammy','Jammy','Sally','Danny'}

# #during class, the teachers take attendance and compile it into a list. 
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

# #using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

# print(school.difference(attendance_list))