#!/bin/python3

# pip install git+https://github.com/not522/ac-library-python
# python -m atcoder main.py -o submit.py

# based on abc185f

import sys
input = sys.stdin.readline
from atcoder.segtree import SegTree

def operation(a, b):
  return a^b

def main():
  n, q = list(map(int, input().strip().split()))
  a = list(map(int, input().strip().split()))

  # SegTree(operation, identity element, init_arr)
  #
  # AtCoder Library Segtree supports non-primitive class
  # Suppose a in A, any method *
  # identity element e should be the one of value which meets
  # 1) a * e = e * a
  # 2) a * e in A
  # for int, e is 0(maybe not supported?), -1, inf(maybe not supported?)
  segtree = SegTree(operation, -1, a)

  for i in range(q):
      t, x, y = list(map(int, input().strip().split()))
      x -= 1

      if t == 1:
        # segtree.get(position)
        tmp = segtree.get(x)
        # segtree.set(position, value)
        segtree.set(x, tmp^y)
      else:
        # segtree.prod(left_position, right_position)
        # returns operation( a[left_position, right_position) )
        print(segtree.prod(x, y))

main()
