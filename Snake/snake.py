from sprite import *

class SnakeBody(Sprite):
  def __init__(self, x, y):
    Sprite.__init__(self, x, y, (0, 255, 0), 15, 15)