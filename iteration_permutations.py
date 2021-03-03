#!/bin/python3

from itertools import permutations

l = [0, 1, 2]
for i in permutations(l):
  print(i)

# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)

for i in permutations(l, 2):
  print(i)

# (0, 1)
# (0, 2)
# (1, 0)
# (1, 2)
# (2, 0)
# (2, 1)

print('---')

for i in permutations(l, 5):
  print(i)

# Blank for i > len(l)
