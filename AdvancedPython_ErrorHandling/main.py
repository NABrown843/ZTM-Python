# Errors in Pythong

# print(1+'hello') # results in TypeError

# def hooohooo() # results in syntax error
#   pass

# KeyErrors, ZeroDivisionError, etc

# Error Handling

# while True:
#   try:
#     age = int(input('what is your age? '))
#     print(age)
#   except ValueError:
#     print('Please enter a number')
#   except ZeroDivisionError:
#     print('Please enter a number higher than zero')
#   else:
#     print('Thank you!')
#     break

  # Error Handling 2

# def sum(num1,num2):
#   try:
#     return num1 + num2
#   except (TypeError,ZeroDivisionError) as err:
#     print(err)
  
# print(sum('1', 2))

# while True:
#   try:
#     age = int(input('what is your age? '))
#     10/age
#   except ValueError:
#     print('Please enter a number')
#     continue
#   except ZeroDivisionError:
#     print('Please enter a number higher than zero')
#     break
#   else:
#     print('Thank you!')
#     break
#   finally:
#     print('ok, I am finally done')
#   print('can you hear me?')

# Error Handling 3

# while True:
#   try:
#     age = int(input('what is your age? '))
#     10/age
#     raise ValueError('hey cut it out')
#   except ZeroDivisionError:
#     print('Please enter a number higher than zero')
#     break
#   else:
#     print('Thank you!')
#     break
#   finally:
#     print('ok, I am finally done')
#   print('can you hear me?')