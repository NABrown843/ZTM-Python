# debugging

# linting
# find errors by read error lines

# using IDE/Editor
# allows detecting errors through highlighting

# Read Errors
# Understand Syntax, Value, Key, etc errors

# PDB
# Python debugger
import pdb

def add(num1, num2):
  pdb.set_trace()
  t= 4* 5
  return num1 + num2

add(4, 'hahdhd')