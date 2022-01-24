# OOP

# class BigObject: # Class
#     #code
#     pass

# obj1 = BigObject() # Instatiate
# obj2 = BigObject() # Instatiate
# obj3 = BigObject() # Instatiate

# print(type(obj1))

# class PlayerCharacter:
#   # Class Object Attribute
#   membership = True
#   def __init__(self, name = 'anonymous', age = 0):
#     self.name = name #attributes
#     self.age = age

#   def shout(self):
#     print(f'my name is {self.name}')

#   def run(self, hello):
#     print(f'my name is {self.name}')

#   @classmethod
#   def adding_things(cls, num1,num2):
#     return num1 + num2

#   @staticmethod
#   def adding_things2(num1,num2):
#     return num1 + num2

# player1 = PlayerCharacter('Cindy', 44)
# player2 = PlayerCharacter('Tom', 10)
# player2.attack = 50

# print(player1)
# print(player2)
# print(player2.run())
# print(player2.age)

# print(player1.attack)
# print(player2.attack)

# help(player1)

# print(player2.membership)

# print(player1.shout())
# print(player2.shout())

# print(player1.run('hello'))

# print(player2.shout())

# print(PlayerCharacter.adding_things(2,3))

# print(PlayerCharacter.adding_things2(2,3))

# Exercise: OOP Cat

# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # 1 Instantiate the Cat object with 3 cats

# cat1 = Cat('Tom', 7)
# cat2 = Cat('Jerry', 1)
# cat3 = Cat('Bluto', 2)

# # 2 Create a function that finds the oldest cat

# def oldest_cat(*args):
#   return max(args)

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# print(f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')

# OOP Review 1

# class NameOfClass():
#   class_attribute = 'value'

#   def __init__(self,param1,param2):
#     self.param1 = param1
#     self.param2 = param2

#   def method(self):
#     #code
#     pass

#   @classmethod
#   def cls_method(cls,param1,param2):
#     #code
#     pass

#   @staticmethod
#   def stc_method(param1,param2):
#     #code
#     pass

# class PlayerCharacter:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   def run(self):
#     return self

# player1 = PlayerCharacter('Joe',100)
# print(player1.run())

# 4 Pillars of OOP
# Encapsulation
# Abstraction
# Inheritance
# Polymorphism

# Encapsulation
# multible objects in class that can be used/called
# shown in previous lessons with methods and attributes in PlayerCharacter

# Abstraction

# how methods/class work can be abstracted from code that calls it

# class PlayerCharacter:
#   def __init__(self,name,age):
#     # No way to make objects private.  Starting with underscore is convention to let other developers not to overwrite
#     self._name = name
#     self._age = age

#   def run(self):
#     print('run')

#   def speak(self):
#     print(f'my name is {self._name}, and I am {self._age} years old')

# player1 = PlayerCharacter('Joe',100)

# print(player1.speak())

# Inheritance
# classes inherit from parent class


# class User:
#     def sign_in(self):
#         print('Logged In')


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')


# # wizard1 = Wizard('Merlin', 50)
# # archer1 = Archer('Robin', 100)
# # wizard1.attack()
# # archer1.attack()

# # isinstance(instance, Class)
# wizard1 = Wizard('Merlin', 60)
# # Inherits from Wizard, User, and Object class
# print(isinstance(wizard1, User))
# print(isinstance(wizard1, object))

# Polymorphism
# Many forms
# method names could be different based on method calling it
# class User:
#     def sign_in(self):
#         print('Logged In')

#     def attack(self):
#       print('do nothing')


# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')

# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 100)

# def player_attack(char):
#   char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#   char.attack()

# Exercise: Pets Everywhere

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Tom(Cat):
#   def sing(self, sounds):
#     return f'{sounds}'

# #1 Add nother Cat

# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon('Simon', 3),Sally('Sally', 2),Tom('Tom', 1)]

# #3 Instantiate the Pet class with all your cats use variable my_pets

# my_pets = Pets(my_cats)

# #4 Output all of the cats walking using the my_pets instance

# my_pets.walk()

# super()

# class User():
#   def __init__(self, email):
#     self.email = email

#   def sign_in(self):
#     print('logged in')

# class Wizard(User):
#     def __init__(self, name, power, email):
#         # User.__init__(self, email)
#         super().__init__(email)
#         self.name = name
#         self.power = power

#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.power}')


# class Archer(User):
#     def __init__(self, name, num_arrows, email):
#         # User.__init__(self, email)
#         super().__init__(email)
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')

# # wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
# # print(wizard1.email)

# # introspection
# wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
# print(dir(wizard1))

# class Toy():
#   def __init__(self, color, age):
#     self.color = color
#     self.age = age
#     self.my_dict = {
#       'name' : 'Yoyo',
#       'has_pets': False
#     }

#   def __str__(self):
#     return f'{self.color}'

#   def __len__(self):
#     return 5

#   def __del__(self):
#     print('deleted!')

#   def __call__(self):
#     print('yess??')

#   def __getitem__(self, i):
#     return self.my_dict[i]


# action_figure = Toy('red', 0)
# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))
# # del action_figure
# print(action_figure())
# print(action_figure['name'])
# print(action_figure['has_pets'])

# Exercise: Extending List

# class SuperList(list):
#   def __len__(self):
#     return 1000


# super_list1 = SuperList();
# print(len(super_list1))
# super_list1.append(5)
# print(super_list1[0])
# print(issubclass(SuperList, list))

# Multiple Inheritance

# class User():
#   def sign_in(self):
#     print('init complete')

# class Wizard(User):
#   def __init__(self, name, power):
#     self.name = name
#     self.power = power

#   def attack(self):
#     print(f'attacking with power of {self.power}')

# class Archer(User):
#   def __init__(self, name, arrows):
#     self.name = name
#     self.arrows = arrows

#   def check_arrows(self):
#     print(f'{self.arrows} remaining')

#   def run(self):
#     print('ran really fast')

# class HybridBorg(Wizard, Archer):
#   def __init__(self, name, power, arrows):
#     Archer.__init__(self, name, arrows)
#     Wizard.__init__(self, name, power)

# hb1 = HybridBorg('Borgie', 50, 100)
# print(hb1.run())
# print(hb1.check_arrows())
# print(hb1.attack())

# Method Resolution Order (MRO)

# class A:
#   num = 10;

# class B(A):
#   pass

# class C(A):
#   num = 1;

# class D(B, C):
#   pass

# print(D.num)

# class X: pass
# class Y: pass
# class Z: pass
# class A(X,Y): pass
# class B(Y,Z): pass
# class M(B,A,Z): pass

# print(M.mro())