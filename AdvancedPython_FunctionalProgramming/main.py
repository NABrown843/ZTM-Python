# Pure Functions

# def multiply_by2(li):
#   new_list = []
#   for item in li:
#     new_list.append(item*2)
#   return new_list

# print(multiply_by2([1,2,3]))

# map()

# def multiply_by2(item):
#   return item*2

# print(list(map(multiply_by2, [1,2,3])))

# filter

# my_list = [1,2,3]

# def only_odd(item):
#   return item % 2 != 0

# print(list(filter(only_odd, my_list)))
# print(my_list)

# zip

# my_list = [1,2,3]
# your_list = [10,20,30]
# their_list = (5,4,3)

# print(list(zip(my_list, your_list, their_list)))
# print(my_list)

# reduce

# from functools import reduce # not part of initial python library; to be explained

# my_list = [1,2,3,4,10]

# def accumulator(acc, item):
#   print(acc, item)
#   return acc + item

# print(reduce(accumulator, my_list, 0))
# print(my_list)

# Exercise: map, filter, zip, reduce

# from functools import reduce

# #1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def capitalize_names(item):
#   return item.capitalize()

# print(list(map(capitalize_names, my_pets)))


# #2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# print(list(zip(my_strings, sorted(my_numbers))))


# #3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def over_50(item):
#   return item > 50

# print(list(filter(over_50, scores)))


# #4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

# def accumulator(acc, item):
#   return acc + item

# print(reduce(accumulator, my_numbers + scores,0))

# lambda expressions

# lambda param: action(param)

# my_list = [1,2,3]

# print(list(filter(lambda item: item % 2 != 0, my_list)))

# Exercise: Lambda Expressions

# Square

# my_list = [5,4,3]

# print(list(map(lambda num: num**2, my_list)))

# List Sorting

# a = [(0,2), (4,3), (9,9), (10,-1)]

# print(sorted(a,key=lambda x: x[1]))

# Comprehensions
# list, set, dictionary

# my_list = []
# for char in 'hello':
#   my_list.append(char)

# print(my_list)

# my_list = [param for param in iterable]

# # list
# my_list = [char for char in 'hello']
# my_list2 = [num for num in range(0,100)]
# my_list3 = [num*2 for num in range(0,100)]
# my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

# # set
# my_list5 = {num**2 for num in range(0,100) if num % 2 == 0}

# # dictionary

# simple_dict = {
#   'a': 1,
#   'b': 2
# }

# my_dict = {k:v**2 for k, v in simple_dict.items()
# if v%2==0}

# my_dict = {num:num*2 for num in [1,2,3]}

# print(my_dict)

# Exercise: Comprehensions

# some_list = ['a','b','c','b','d','m','n','n']

# duplicates = {char for char in some_list if some_list.count(char) > 1} # my solution

# duplicates = list(set([x for x in some_list if some_list.count(x) > 1])) # Andrei's Solution

# print(list(duplicates))