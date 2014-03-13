#!/bin/python

def displayPathtoPrincess(n,grid):

  # set at n = 3 (3x3 grid)
  # need to integrate the 0 as an iterable
  # so that the grid size can change
  # coordinates 0,0 break also... 
  
  center = [n - (2 + 0), n - (2 + 0)]
  
  direction_vertical = "off"
  direction_horizontal = "off"
  
  mv1, mv2 = center[0], grid[0]
  mh1, mh2 = center[1], grid[1]
  
  move_vertical = mv1 - mv2
  move_horizontal = mh1 - mh2
  
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
