# Generators

# range(100)
# list(range(100))

# def make_list(num):
#   result = []
#   for i in range(num):
#     result.append(i*2)
#   return result

# my_list = make_list(100)
# print(list(range(100)))

# Generators 2
# iterable
# generators are subsets of iterables

# def generator_function(num):
#   for i in range(num):
#     yield i*2

# # for item in generator_function(1000):
# #   print(item)

# g = generator_function(100)
# next(g)
# next(g)
# print(next(g))

# from time import time

# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'function took {t2-t1} ms.')
#     return result
#   return wrapper

# @performance
# def long_time():
#   print('1')
#   for i in range(100000000):
#     i*5

# @performance
# def long_time2():
#   print('2')
#   for i in list(range(100000000)):
#     i*5

# long_time()
# long_time2()

# def gen_fun(num):
#   for i in range(num):
#     yield i

# Under the hood of generators

# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       print(iterator)
#       print(next(iterator)*2)
#     except StopIteration:
#       break

# special_for([1,2,3])

# class MyGen():
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
  
#   def __iter__(self):
#     return self

#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration

# gen = MyGen(0,100)
# for i in gen:
#   print(i)

# Exercise: Fibonacci Numbers

def fib(number):
  a = 0
  b = 1
  for i in range(number):
    yield a
    temp = a
    a = b
    b = temp + b

for x in fib(21):
  print(x)