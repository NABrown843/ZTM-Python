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

from datetime import date

birth_year = input('What year were you born? ')
age = date.today().year - int(birth_year)
print(f'Your age is {age}.')