#!/bin/python3

import sys

def min_magic(max_height, heights):
  diff = sorted(heights)[-1] - max_height
  return diff if diff > 0 else 0

def main():
  n, k = map(int, input().strip().split(' '))
  heights = list(map(int, input().strip().split(' ')))
  print(min_magic(k, heights))

if __name__ == "__main__":
  main()
