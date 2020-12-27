#!/bin/python3

from atcoder.fenwicktree import FenwickTree

n = int(input().strip())
tree = FenwickTree(n)

for i in range(n):
  tree.add(i, 1)

# AtCoder Library doesn't have get API.
# Insted you can use sum with span 1.
j = 3
print(tree.sum(j, j+1))

# return the sum of a[l, r)
print(tree.sum(0, n))
