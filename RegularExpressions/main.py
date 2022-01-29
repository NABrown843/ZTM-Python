import re

# pattern = re.compile('this')
# string = 'search inside of this text please!'

# # print('search' in string)

# a = re.search('this', string)
# b = pattern.search(string)
# c = pattern.findall(string)
# d = pattern.fullmatch(string)
# e = pattern.match(string)

# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# pattern = re.compile('"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"')

# pattern = re.compile(r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)')

# string = 'blah@blah.com'

# a = pattern.search(string)
# print(a)

# At least 8 char long
# contain any sort letters, numbers, $%#@
# has to end with a number

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d$")
password = 'hada'

check = pattern.fullmatch(password)
print(check)