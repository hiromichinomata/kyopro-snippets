#!/bin/python3

from collections import deque

def main():
  d = deque()
  d.append(1)
  d.appendleft(2)
  v = d.pop()
  print(v)
  v = d.popleft()
  print(v)

main()
