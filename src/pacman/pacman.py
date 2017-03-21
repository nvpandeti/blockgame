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

WIDTH = 300
HEIGHT = 330

def posDisp(posi, dir, disp):
    pos = Point(posi.x, posi.y)
    if(dir == UP):
        pos.y += -disp
    elif(dir == LEFT):
        pos.x += -disp
    elif(dir == DOWN):
        pos.y += disp
    elif(dir == RIGHT):
        pos.x += disp
    return pos

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
        elif(self.dir == RIGHT):
            self.pos.x += 1
        return self.pos.inBounds()

class Pacman(GameObject):
    def __init__(self, x, y, dir):
        GameObject.__init__(self, x, y, dir)
        self.newDir = STUCK
    def move(self):
        print(self.pos.x, self.pos.y, self.dir, self.newDir, ' |', end='')
        self.pos.x %= WIDTH
        self.pos.y %= HEIGHT
        if(self.pos.x % 10 == 0 and self.pos.y % 10 == 0):
            if(self.newDir != STUCK):
                newP = posDisp(self.pos, self.newDir, 10)
                if(walls_map[(newP.x//10)%30][(newP.y//10)%33] == False):
                    self.dir = self.newDir
                    self.newDir = STUCK
            newP = posDisp(self.pos, self.dir, 10)
            if(walls_map[(newP.x//10)%30][(newP.y//10)%33]):
                self.newDir = self.dir
                self.dir = STUCK
        GameObject.move(self)
        print(self.pos.x, self.pos.y, self.dir, self.newDir)
        
    def changeDir(self, dir):
        self.newDir = dir
    def render(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.pos.x+5, self.pos.y+5), 5)
    def clear(self, screen):
        pygame.draw.circle(screen, BLACK, (self.pos.x+5, self.pos.y+5), 5)
    
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
    screen.fill(BLACK)
    for i in range(len(walls_map)):
        for j in range(len(walls_map[i])):
            if(walls_map[i][j]):
                pygame.draw.rect(screen, BLUE, (i*10, j*10, 10, 10), 0)
    pac = Pacman(140, 240, STUCK)
    while x == False:
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = True
                pygame.quit
            if event.type == pygame.MOUSEBUTTONUP:
                click = True
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                    pac.changeDir(RIGHT)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    pac.changeDir(DOWN)
                elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                    pac.changeDir(LEFT)
                elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                    pac.changeDir(UP)
        (mx,my) = pygame.mouse.get_pos()
        #print(mx, my)
        pac.move()
        
        pac.render(screen)
        pygame.display.flip()
        clock.tick(40)
        pac.clear(screen)
    pygame.quit()
    
main()    