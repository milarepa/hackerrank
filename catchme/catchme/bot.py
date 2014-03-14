#!/bin/python

class Zelda:
  'Solving the problem of using a bot to find a target'

  def __init__(self, gridsize, target, adj):
    self.target = target
    self.gridsize = gridsize
    self.adj = adj
    self.center = []



  def acquire(self):

    self.center = Zelda.findCenter(self, self.gridsize, self.adj, self.target)

    direction_vertical = "off"
    direction_horizontal = "off"

    # move from the center
    mv1, mv2 = self.center[0], self.target[0]
    mh1, mh2 = self.center[1], self.target[1]

    move_vertical = mv1 - mv2
    move_horizontal = mh1 - mh2

    directions = []

    if move_vertical < 0:
      direction_vertical = "RIGHT"
      steps_vertical = -(move_vertical)
    else:
      direction_vertical = "LEFT"
      steps_vertical = move_vertical

    if move_horizontal < 0:
      direction_horizontal = "DOWN"
      steps_horizontal = -(move_horizontal)
    else:
      direction_horizontal = "UP"
      steps_horizontal = move_horizontal

    for i in range(steps_vertical):
      directions.append(direction_vertical)

    for j in range(steps_horizontal):
      directions.append(direction_horizontal)
      
    return directions


  def findCenter(self, gridsize, adj, target):

    c = gridsize - (2 + adj)
    if target[0] == 0 and target[1] == 0:
      center = [-(c), -(c)]
    else:
      center = [c, c]

    return center





"""


m = input()
grid = []
for i in xrange(0,m):
  grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
"""
