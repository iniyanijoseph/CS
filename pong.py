import pygame
pygame.init()

win = pygame.display.set_mode((500, 300))
players = []
run=True

class LeftSide(object):
  def __init__(self):
    self.x = 10
    self.y = 10
    self.velocity = [0, 0]
    self.width = 10
    self.height = 40
  
  def update(self):
    self.velocity = [0, 0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and self.y > 0:
      self.velocity[1] -= 4
    if keys[pygame.K_s] and self.y +self.height< 300:
      self.velocity[1] += 4
    
    self.x += self.velocity[0]
    self.y += self.velocity[1]
  
  def draw(self):
    pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

class RightSide(object):
  def __init__(self):
    self.x = 490
    self.y = 10
    self.velocity = [0, 0]
    self.width = 10
    self.height = 40
  
  def update(self):
    self.velocity = [0, 0]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.y > 0:
      self.velocity[1] -= 4
    if keys[pygame.K_DOWN] and self.y +self.height < 300:
      self.velocity[1] += 4
    
    self.x += self.velocity[0]
    self.y += self.velocity[1]
    

  
  def draw(self):
    pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Ball(object):
  def __init__(self):
    self.x = 250
    self.y = 10
    self.velocity = [2, 2]
    self.radius = 10
  
  def update(self):
    for each in players:
      if self.x == each.x:
        if self.y > each.y and self.y < each.y + each.height:
          self.velocity[0] *= -1
    if 500 < self.x or self.x < 0:
        exit()
    
    if self.y > 300 - self.radius*2 or self.y < 0:
        self.velocity[1] *= -1
    self.x += self.velocity[0]
    self.y += self.velocity[1]
      
  
  def draw(self):
    pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)


players.append(LeftSide())
players.append(RightSide())
ball = Ball()


clock=pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    win.fill((0,0,0))
    #win.blit("backgroundpic.png")
    for element in players:
        element.update()
        element.draw()
    ball.update()
    ball.draw()
    pygame.display.update()
pygame.display.quit()

