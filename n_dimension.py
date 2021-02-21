#!/bin/python3

import sys
input = sys.stdin.readline

def convert(s, n):
  result = 0
  s_i = list(reversed([int(char) for char in str(s)]))
  for i in range(len(s_i)):
    result += s_i[i] * (n**i)
  return result

def main():
  result = convert('1001', 14)
  print(result)
  # => 2745

main()
