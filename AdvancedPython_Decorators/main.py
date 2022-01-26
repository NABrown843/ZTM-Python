# def hello(func):
#   func()

# def greet():
#   print('still here!')

# a = hello(greet)

# print(a)

# Higher Order Function HOC

# def greet(func):
#   func()
# map()
# filter()
# def greet2():
#   def func():
#     return 5
#   return func

# Decorator

# def my_decorator(func):
#   def wrap_func(*args, **kwargs):
#     print('***********')
#     func(*args, **kwargs)
#     print('***********')
#   return wrap_func

# # @my_decorator
# # def hello():
# #   print('hellloooo')

# @my_decorator
# def hello(greeting):
#   print(greeting)

# # @my_decorator
# # def bye():
# #   print('see ya later')

# hello('hellloooo')

# # bye()

# Performance Decorator

# from time import time

# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2 - t1} ms')
#     return result
#   return wrapper

# @performance
# def long_time():
#   for i in range(100000000):
#     i*5

# long_time()

# Exercise: @authenticated

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#   def wrapper(*args,**kwargs):
#     if args[0]['valid']:
#       return fn(*args,**kwargs)
#   return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)