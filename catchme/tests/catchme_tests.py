#!/usr/bin/python3
from nose.tools import *
from catchme.bot import Zelda

def test_center():

  bot = Zelda(9, [6,7], 3)
  test_center = bot.findCenter(bot.gridsize, bot.adj, bot.target)

  bot1 = Zelda(9, [0,0], 3)
  test_center1 = bot1.findCenter(bot1.gridsize, bot1.adj, bot1.target)

  assert_equal(bot.gridsize, 9)
  assert_equal(bot.adj, 3)
  assert_equal(bot1.gridsize, 9)
  assert_equal(bot1.adj, 3)

  assert_equal(bot.target, [6,7])
  assert_equal(bot1.target, [0,0])

  assert_equal(test_center, [4,4])
  assert_equal(test_center1, [-4,-4])



def test_acquire():
  
  # this test should result in a list of 3 right and 2 down
  bot = Zelda(9,[6,7],3)
  directions = bot.acquire()
  
  assert_equal(bot.center, [-4, -4])
  
  assert_equal(bot.mv1, 4)
  assert_equal(bot.mv2, 6)
  
  assert_equal(bot.mh1, 4)
  assert_equal(bot.mh2, 7)
  
  assert_equal(bot.move_vertical, -2)
  assert_equal(bot.move_horizontal, -3)
  
  assert_equal(bot.move_vertical < 0, True)
  assert_equal(bot.move_horizontal < 0, True)
  
  assert_equal(bot.steps_vertical, 2)
  assert_equal(bot.steps_horizontal, 3)
  
  
  
  
