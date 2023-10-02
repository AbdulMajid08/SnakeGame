from processing import *

# modified to use rect in disply

class Sprite:
  def __init__(self, x, y, c, w, h):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.color = c
  

  def display(self):
    fill(*self.color)
    rect(self.x, self.y, self.w, self.h)


  def move(self, xs, ys):
    self.x += xs
    self.y += ys



  def collision(self, item):
    right = self.x < item.x + item.w
    left = self.x + self.w > item.x
    down = self.y < item.y + item.h
    up = self.y + self.h > item.y
    collided = right and left and down and up
    return collided