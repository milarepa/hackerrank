#!/bin/python

def displayPP(n,grid):

  # set at n = 3 (3x3 grid)
  # need to integrate the 0 as an iterable
  # so that the grid size can change
  # coordinates 0,0 break also...

  adj = 3
  c = n - (2 + adj)

  if grid[0] == 0 and grid[1] == 0:
    center = [-(c), -(c)]
  else:
    center = [c,c]

  direction_vertical = "off"
  direction_horizontal = "off"

  # move from the center
  mv1, mv2 = center[0], grid[0]
  mh1, mh2 = center[1], grid[1]

  move_vertical = mv1 - mv2
  move_horizontal = mh1 - mh2

  #directions = []

  if move_vertical < 0:
    direction_vertical = "LEFT"
    steps_vertical = -(move_vertical)
  else:
    direction_vertical = "RIGHT"
    steps_vertical = move_vertical

  if move_horizontal < 0:
    direction_horizontal = "UP"
    steps_horizontal = -(move_horizontal)
  else:
    direction_horizontal = "DOWN"
    steps_horizontal = move_horizontal

  for i in range(steps_vertical):
    print direction_vertical

  for j in range(steps_horizontal):
    print direction_horizontal








"""


m = input()
grid = []
for i in xrange(0,m):
  grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
"""
