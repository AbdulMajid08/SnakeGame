from processing import *
from snake import *
from apple import *
from random import *


SNAKE_VELOCITY = 15    # velocity needs to be the same as rect w,h so bodies dont overlap?
moveDir = "none"
tickTimer = 0
ap = Apple(200, 200)
snakelst = []
snakelst.append(SnakeBody(100, 100))     # head is at snakelst[0]

def setup():
  size(500, 500)
  
  
  
  
def draw():
  global moveDir, tickTimer, newBody
  tickTimer += 1
  
  background(0, 0, 0)
  ap.display()
  
  for i in snakelst:
    i.display()
    
    
    
    
    
  if snakelst[0].collision(ap):     # if the head of the snake touches the apple
    # create new snake at location of last SnakeBody in list, and append to list
    snakelst.append(SnakeBody(snakelst[-1].x, snakelst[-1].y))   

    # move apple to new random spot, within screen and multiple of velocity
    ap.x = randint(0,500)
    ap.y = randint(0,500)
    #ap.x = randint(0, width // SNAKE_VELOCITY) * SNAKE_VELOCITY
    #ap.y = randint(0, height // SNAKE_VELOCITY) * SNAKE_VELOCITY

  
  if tickTimer > 5:
    for i in range(len(snakelst) - 1, 0, -1):   # countdown from end of snakelst to 1. dont need to check for if len is > 1 because range will ignore if isnt
      snakelst[i].x = snakelst[i - 1].x         # move current snake to the position of the previous one in the list
      snakelst[i].y = snakelst[i - 1].y
    
    if moveDir == "up":                         # move the head
      snakelst[0].move(0, -SNAKE_VELOCITY)
    elif moveDir == "down":
      snakelst[0].move(0, SNAKE_VELOCITY)
    elif moveDir == "right":
      snakelst[0].move(SNAKE_VELOCITY, 0)
    elif moveDir == "left":
      snakelst[0].move(-SNAKE_VELOCITY, 0)
    #else:
    #  pass         # dont move
  
    for i in range(1, len(snakelst)):             # check if head collides with other SnakeBody. has to be after and in tick so it doesnt collide with the second body
      if snakelst[0].collision(snakelst[i]):
        text("game over", 100, 100)
        exit()
  
  
    tickTimer = 0
  


  
  
  if keyPressed:
    if key == CODED:
      if keyCode == UP and moveDir != "down":
        moveDir = "up"
      if keyCode == DOWN and moveDir != "up":
        moveDir = "down"
      if keyCode == RIGHT and moveDir != "left":
        moveDir = "right"
      if keyCode == LEFT and moveDir != "right":
        moveDir = "left"
  
  
run()





















