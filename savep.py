#!/bin/python

def displayPathtoPrincess(n,grid):

  # set at n = 3 (3x3 grid)
  center = [n - (2 + 0), n - (2 + 0)]

  move_vertical = center[0] - grid[0]
  print(move_vertical),

  move_horizontal = center[1] - grid[1]
  print(move_horizontal),










"""


m = input()
grid = []
for i in xrange(0,m):
  grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
"""
