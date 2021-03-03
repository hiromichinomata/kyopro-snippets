#!/bin/python3

from itertools import product

for i in product('ABCD', repeat=2):
  print(i)

# ('A', 'A')
# ('A', 'B')
# ('A', 'C')
# ('A', 'D')
# ('B', 'A')
# ('B', 'B')
# ('B', 'C')
# ('B', 'D')
# ('C', 'A')
# ('C', 'B')
# ('C', 'C')
# ('C', 'D')
# ('D', 'A')
# ('D', 'B')
# ('D', 'C')
# ('D', 'D')

print('')

for i in product('AB', 'CD'):
  print(i)

# ('A', 'C')
# ('A', 'D')
# ('B', 'C')
# ('B', 'D')

print('')

for i in product('AB', 'CD', repeat=2):
  print(i)

# ('A', 'C', 'A', 'C')
# ('A', 'C', 'A', 'D')
# ('A', 'C', 'B', 'C')
# ('A', 'C', 'B', 'D')
# ('A', 'D', 'A', 'C')
# ('A', 'D', 'A', 'D')
# ('A', 'D', 'B', 'C')
# ('A', 'D', 'B', 'D')
# ('B', 'C', 'A', 'C')
# ('B', 'C', 'A', 'D')
# ('B', 'C', 'B', 'C')
# ('B', 'C', 'B', 'D')
# ('B', 'D', 'A', 'C')
# ('B', 'D', 'A', 'D')
# ('B', 'D', 'B', 'C')
# ('B', 'D', 'B', 'D')

print('')

for i in product([True, False], repeat=3):
  print(i)

# (True, True, True)
# (True, True, False)
# (True, False, True)
# (True, False, False)
# (False, True, True)
# (False, True, False)
# (False, False, True)
# (False, False, False)
