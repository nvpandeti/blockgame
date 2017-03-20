'''
Created on Mar 4, 2017

@author: nikhil
'''
import pygame
import math

BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
ORANGE = ( 255, 128,   0)
YELLOW = ( 255, 255,   0)
PINK   = ( 125,   0,   0)
CYAN   = (   0, 255, 255)

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
STUCK = 4

WIDTH = 15
HEIGHT = 15

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def inBounds(self):
        return self.x >= 0 and self.y >= 0 and self.x < WIDTH and self.y < HEIGHT 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class GameObject():
    def __init__(self, x, y, dir):
        self.pos = Point(x, y)
        self.dir = dir
    def setDir(self, dir):
        self.dir = dir;
    def move(self):
        if(self.dir == UP):
            self.pos.y += -1
        elif(self.dir == LEFT):
            self.pos.x += -1
        elif(self.dir == DOWN):
            self.pos.y += 1
        elif(self.pos == RIGHT):
            self.pos.x += 1
        return self.pos.inBounds()

class Pacman(GameObject):
    def __init__(self, x, y, dir):
        GameObject.__init__(self, x, y, dir)
    def move(self, walls):
        GameObject.move(self)
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT
        for wall in walls:
            if(wall.pos == self.pos):
                return False
        return True
    def render(self, screen):
        pass
    
class Ghost(GameObject):
    def __init__(self, x, y, dir, color):
        GameObject.__init__(self, x, y, dir)
        self.color = color
        self.scared = False
    def move(self):
        if(self.color == RED):
            pass
        elif(self.color == ORANGE):
            pass
        elif(self.color == CYAN):
            pass
        else:
            print("CLYDE!")

class Wall(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, STUCK)
    def render(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 10, 10), 0)

walls_map = [[False for y in range(33)] for x in range(30)]
walls_map = [[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 
             [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 
             [True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, True, True, False, False, False, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True], 
             [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, False, True, True, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True], 
             [True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, False, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True], 
             [True, True, False, True, True, True, False, True, True, False, True, True, False, True, False, False, False, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, False, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, True, True, True, False, True, True], 
             [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True], 
             [True, True, False, True, True, True, False, True, False, True, True, True, True, True, True, False, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True], 
             [True, True, False, False, False, False, False, False, False, True, True, True, True, True, True, False, True, True, True, True, True, False, False, False, False, True, True, False, False, False, False, True, True], 
             [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True], 
             [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]]
 
              

def main():
    pygame.init()
    screen = pygame.display.set_mode([300, 330])
    pygame.display.set_caption('PACMAN')
    font = pygame.font.Font(None,30)
    clock = pygame.time.Clock()
    x = False
    mx = 0
    my = 0
    while x == False:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = True
                pygame.quit
            if event.type == pygame.MOUSEBUTTONUP:
                click = True

        screen.fill(BLACK)
        for i in range(len(walls_map)):
            for j in range(len(walls_map[i])):
                if(walls_map[i][j]):
                    pygame.draw.rect(screen, BLUE, (i*10, j*10, 10, 10), 0)
        pygame.display.flip()
        clock.tick(25)
    pygame.quit()
    
main()    