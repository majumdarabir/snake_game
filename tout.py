
import pygame 
from pygame.locals import *
import time
import random
SIZE=40

class Wallpaper:
  def __init__(self,surface):
    self.surface=surface
    self.pic=pygame.image.load('resources/coverpage2.jpg').convert()
    self.surface.blit(self.pic,(0,0))
    
    pygame.display.flip()
    time.sleep(0.5)
    


class Apple:
    def __init__(self,surface):
        self.parent_screen=surface
        self.image=pygame.image.load('resources/apple4.jpg').convert()
        self.x=120
        self.y=120
    def draw(self):
         self.parent_screen.blit(self.image,(self.x,self.y))
         pygame.display.flip()
    def move(self):
         self.x=random.randint(1,9)*SIZE
         self.y=random.randint(1,9)*SIZE
         


class Snake:
    def __init__(self, surface,length):
       self.parent_screen=surface
       pygame.display.set_caption("@created by Abir!")
       self.block=pygame.image.load('resources/block4.png').convert()
       self.length=length
       self.x=[40]*length
       self.y=[40]*length
       self.direction='down' 
    def move_left(self):
        self.direction='left'
    def move_right(self):
        self.direction='right'
    def move_up(self):
        self.direction='up'
    def move_down(self):
        self.direction='down'
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
        

    def walk(self):
        for i in range (self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        if self.direction=='left':
           self.x[0]-=40
        elif self.direction=='right':
           self.x[0]+=40
        elif self.direction=='up':
           self.y[0]-=40
        elif self.direction=='down':
           self.y[0]+=40
        self.draw()
    def draw(self):
      self.image=pygame.image.load('resources/background6.jpg').convert()
      self.parent_screen.blit(self.image,(0,0))
      for i in range(self.length):
        self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
      pygame.display.flip()
class Game:
     def __init__(self):
       pygame.init()
       pygame.mixer.init()
       self.surface=pygame.display.set_mode((400,400))
       self.wallpaper=Wallpaper(self.surface)
       self.image=pygame.image.load('resources/background6.jpg').convert()
       self.surface.blit(self.image,(0,0))
       
       
       self.snake=Snake(self.surface,1)
       self.snake.draw()
       self.apple=Apple(self.surface)
       self.apple.draw()
     def restart(self):
         
         self.snake=Snake(self.surface,1)
         
         self.apple=Apple(self.surface)
         
         


     def score(self):
         font=pygame.font.SysFont('arial',30)
         score=font.render(f"score:{self.snake.length}",True,(255,0,0))
         self.surface.blit(score,(300,10))
     def show_gameover(self):
         self.surface.blit(self.image,(0,0))
         font=pygame.font.SysFont('arial',30)
         line1=font.render(f'Game is over,Your score:{self.snake.length}',True,(200,200,200))
         self.surface.blit(line1,(50,100))
         font=pygame.font.SysFont('arial',30)
         line2=font.render('press Enter to play again',True,(200,200,200))
         self.surface.blit(line2,(50,150))
         
         pygame.display.flip()

     def is_collision(self,x1,y1,x2,y2):
        if x1>=x2 and x1<x2+SIZE:
          if y1>=y2 and y1<y2+SIZE:
            return True
     
        return False
     def play(self):
         self.snake.walk()
         self.apple.draw()
         #snake collition with Apple
         
         for i in range(self.snake.length):
           if self.is_collision(self.snake.x[i],self.snake.y[i],self.apple.x,self.apple.y):
               
               self.snake.increase_length()
               self.apple.move()
               
               
         if not ((0<=self.snake.x[0]<=399) and (0<=self.snake.y[0]<=399)):  
           raise "hit the wall game over"
         self.score()
         pygame.display.flip()
        
         #snake collision with itself
         for i in range(1,self.snake.length):
             if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                 raise "GAME OVER"

     def run(self):
      running=True
      pause=False
      while running:
        for event in pygame.event.get():
          if event.type==KEYDOWN:
            
              if event.key==K_ESCAPE:
                  running= False
              if event.key==K_RETURN:
                  pause=False
                  self.restart()
              if not pause: 
                if event.key==K_RIGHT:
                  
                  self.snake.move_right()
                elif event.key==K_LEFT:
                  
                  self.snake.move_left()
                elif event.key==K_UP:
                  
                  self.snake.move_up()
                elif event.key==K_DOWN:
                  
                  
                  self.snake.move_down()

        


          if event.type==QUIT:
            running=False
        try:
         if not pause:
          self.play()
        except Exception as e:
          self.show_gameover()
          pause=True
        
        
        
        time.sleep(0.1)

if __name__=='__main__':
  game=Game()
  game.run()
    