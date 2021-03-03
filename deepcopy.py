#!/bin/python3

import copy

def main():
  a = [[1, 2], [3, 4]]
  a_copied = a
  a_deep_copied = copy.deepcopy(a)
  a[0][0] = 999

  print(a_copied)
  print(a_deep_copied)

main()
