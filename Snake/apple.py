from sprite import *


class Apple(Sprite):
  def __init__(self, x, y):
    Sprite.__init__(self, x, y, (255, 0, 0), 15, 15)

