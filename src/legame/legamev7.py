'''
Created on Apr 19, 2016

@author: Nitu
'''
import pygame
import math
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
PURPLE = ( 255,   0, 255)
class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
    def __init__(self, x, y, width, height, color, direction):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.color = color
        self.image.fill(self.color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.direction = direction
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player controls """
    # Set speed vector
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.color = WHITE
        self.image.fill(self.color)
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.health = 100
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x  += x
        self.change_y  += y
    def move(self, walls):
        """ Find a new position for the player """
        # Move left/right
        self.rect.x += self.change_x
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # Move up/down
        self.rect.y += self.change_y
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
    def getX(self):
        return self.rect.x
    def getY(self):
        return self.rect.y
    def NoobToob(self,screen,mousex,mousey):
        mousex = float(mousex)
        mousey = float(mousey)
        mousex = mousex-self.rect.center[0]
        mousey = mousey-self.rect.center[1]
        self.mousex2 = math.cos(math.atan2(mousey,mousex))*17
        self.mousey2 = math.sin(math.atan2(mousey,mousex))*17
        pygame.draw.line(screen,WHITE,self.rect.center,(self.rect.center[0]+self.mousex2,self.rect.center[1]+self.mousey2),5)
    def Health(self, screen):

        #pygame.draw.rect(screen,color,[x coordinate, y coordinate, width, height],width of edges)
        pygame.draw.rect(screen,RED,[self.rect.center[0]-((self.health/100)*30)/2,self.rect.center[1]-13,(self.health/100)*30,3],0)
        if self.health<=0:
            self.kill()

                        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, changex, changey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.color = RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        #self.rect.y = y
        #self.rect.x = x
        self.rect.center = (x,y)
        self.change_x = changex//2
        self.change_y = changey//2
    def move(self, walls, nazi_list):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if block.color != WHITE:
                block.kill()
        for block in block_hit_list:
            self.kill()
        block_hit_list = pygame.sprite.spritecollide(self, nazi_list, False)
        for block in block_hit_list:
            block.kill()
        for block in block_hit_list:
            self.kill()
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if block.color != WHITE:
                block.kill()
        for block in block_hit_list:
            self.kill()
        block_hit_list = pygame.sprite.spritecollide(self, nazi_list, False)
        for block in block_hit_list:
            block.kill()
        for block in block_hit_list:
            self.kill()



class BounceBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, changex, changey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.color = RED
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        #self.rect.y = y
        #self.rect.x = x
        self.rect.center = (x,y)
        self.change_x = changex//2
        self.change_y = changey//2
        self.bounce = 2
    def move(self, walls, nazi_list):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if block.color != WHITE:
                block.kill()
        for block in block_hit_list:
            if self.bounce == 0:
                self.kill()
            self.bounce = self.bounce-1
            if(block.direction == 'v'):
                self.change_x = -(self.change_x)
            if(block.direction == 'h'):
                self.change_y = -(self.change_y)
        block_hit_list = pygame.sprite.spritecollide(self, nazi_list, False)
        for block in block_hit_list:
            block.kill()
        for block in block_hit_list:
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, changex, changey):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([3, 3])
        self.color = GREEN
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.change_x = changex//2
        self.change_y = changey//2
    def move(self, walls,movingsprites):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        #for block in block_hit_list:
        #    if block.color != WHITE:
        #        block.kill()
        for block in block_hit_list:
            self.kill()
        block_hit_list = pygame.sprite.spritecollide(self, movingsprites, False)
        for block in block_hit_list:
            if isinstance(block, Player):
                print("T")
                block.health=block.health-20
            else:
                print("F")
                block.kill()
        for block in block_hit_list:
            self.kill()

class Nazi(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15, 15])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def move(self, walls, movingsprites, center, nazi_list):
        if center[0] - self.rect.center[0] < 0:
            self.change_x += -.1
        elif center[0] - self.rect.center[0] > 0:
            self.change_x += .1
        if center[1] - self.rect.center[1] < 0:
            self.change_y += -.1
        elif center[1] - self.rect.center[1] > 0:
            self.change_y += .1
        self.rect.x += self.change_x
        if self.change_x>7:
            self.change_x = 7
        if self.change_x<-7:
            self.change_x = -7
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if block.color == WHITE:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        block_hit_list = pygame.sprite.spritecollide(self, movingsprites, False)
        for block in block_hit_list:
            if block.color == WHITE:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        block_hit_list = pygame.sprite.spritecollide(self, nazi_list, False)
        for block in block_hit_list:
            if block != self:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
        self.rect.y += self.change_y
        if self.change_y>7:
            self.change_y = 7
        if self.change_y<-7:
            self.change_y = -7
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if block.color == WHITE:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom
        block_hit_list = pygame.sprite.spritecollide(self, movingsprites, False)
        for block in block_hit_list:
            if block.color == WHITE:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom
        block_hit_list = pygame.sprite.spritecollide(self, nazi_list, False)
        for block in block_hit_list:
            if block != self:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom
    def NoobToob(self,screen, center):
        mousex = center[0]-self.rect.center[0]
        mousey = center[1]-self.rect.center[1]
        self.mousex2 = math.cos(math.atan2(mousey,mousex))*17
        self.mousey2 = math.sin(math.atan2(mousey,mousex))*17
        pygame.draw.line(screen,RED,self.rect.center,(self.rect.center[0]+self.mousex2,self.rect.center[1]+self.mousey2),5)
    def fire(self):
        return True
Room1_walls = [[0, 0, 20, 800, WHITE,'v'],
               [580, 0, 20, 800, WHITE,'v'],
               [200, 250, 20, 550, WHITE,'v'],
               [260, 250, 20, 550, WHITE,'v'],
               [430, 250, 20, 550, WHITE,'v'],
               [230, 50, 20, 500, BLUE,'v'],
               [195, 50, 20, 500, BLUE,'v'],
               [430, 20, 150, 20, BLUE, 'h'],
               [430, 60, 150, 20, BLUE, 'h'],
               [430, 100, 150, 20, BLUE,'h']]
Room2_walls = [[0, 0, 20, 800, WHITE, 'v'],
               [580, 0, 20, 800, WHITE, 'v'],
               [300, 300, 20, 100, WHITE, 'v'],
               [500, 300, 20, 100, WHITE, 'v'],
               [300, 400, 220, 20, WHITE, 'h'],
               [300, 500, 20, 110, WHITE, 'v'],
               [0, 780, 600, 20, WHITE, 'h']]
Room3_walls = [[0, 0, 600, 20, WHITE, 'h'],
               [0, 0, 20, 800, WHITE, 'v'],
               [580, 0, 20, 800, WHITE, 'v'],
               [500, 200, 20, 200, WHITE, 'v'],
               [500, 400, 100, 20, WHITE, 'h'],
               [500, 400, 20, 200, WHITE, 'v'],
               [100, 400, 20, 200, WHITE, 'v'],
               [100, 400, 200, 20, WHITE, 'h'],
               [100, 200, 20, 200, WHITE, 'v']]

class Room(object):
    """ Base class for all rooms. """
    """ Each room has a list of walls, and of enemy sprites. """
    wall_list = None
    enemy_sprites = None
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
class Room1(Room):
    """This creates all the walls in room 1"""
    def __init__(self):
        Room.__init__(self)
        # Make the walls. (x_pos, y_pos, width, height)
        # This is a list of walls. Each is in the form [x, y, width, height]
# nikhil is a punk bitch 
        # Loop through the list. Create the wall, add it to the list
        for item in Room1_walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
        for item in Room2_walls:
            wall = Wall(item[0], item[1]+800, item[2], item[3], item[4], item[5] )
            self.wall_list.add(wall)
        for item in Room3_walls:
            wall = Wall(item[0], item[1]-800, item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
class Room2(Room):
    """This creates all the walls in room 2"""
    def __init__(self):
        Room.__init__(self)
        for item in Room2_walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
        for item in Room3_walls:
            wall = Wall(item[0], item[1]-1600, item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
        for item in Room1_walls:
            wall = Wall(item[0], item[1]-800, item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)


class Room3(Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        Room.__init__(self)
        for item in Room3_walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
        for item in Room1_walls:
            wall = Wall(item[0], item[1]+800, item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)
        for item in Room2_walls:
            wall = Wall(item[0], item[1]+1600, item[2], item[3], item[4], item[5])
            self.wall_list.add(wall)

def main():
    """ Main Program """
    # Call this function so the Pygame library can initialize itself
    pygame.init()
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([600, 800])
    # Set the title of the window
    pygame.display.set_caption('THE GAME')
    font = pygame.font.Font(None,30)
    youWin = font.render("You Win", True, PURPLE)
    youLose = font.render("You're a loser and your mom doesn't love you, NIKHIL LIKES MEN", True, PURPLE)
    # Create the player paddle object
    movingsprites = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    enemybullet_list = pygame.sprite.Group()
    nazi_list = pygame.sprite.Group()
    player = Player(50, 50)
    movingsprites.add(player)
    nazi = Nazi(400,400)
    nazi_list.add(nazi)
    nazi = Nazi(500,500)
    nazi_list.add(nazi)
    nazi = Nazi(500,400)
    nazi_list.add(nazi)
    nazi = Nazi(400,500)
    nazi_list.add(nazi)
    rooms = []
    room = Room1()
    rooms.append(room)
    room = Room2()
    rooms.append(room)
    room = Room3()
    rooms.append(room)
    current_room_no = 0
    current_room = rooms[current_room_no]
    clock = pygame.time.Clock()
    done = False
    num = 0
    while not done:
        # --- Event Processing ---
        (mousex,mousey) = pygame.mouse.get_pos()
        for event in pygame.event.get():
            mousekeys = pygame.mouse.get_pressed()
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.changespeed(0, 5)
            if event.type == pygame.MOUSEBUTTONDOWN and movingsprites.has(player) and ( mousekeys[0] or mousekeys[1]):
                bullet = Bullet(player.rect.center[0],player.rect.center[1],player.mousex2,player.mousey2)
                movingsprites.add(bullet)
                bullet_list.add(bullet)
            if event.type == pygame.MOUSEBUTTONDOWN and movingsprites.has(player) and mousekeys[2]:
                bullet = BounceBullet(player.rect.center[0],player.rect.center[1],player.mousex2,player.mousey2)
                movingsprites.add(bullet)
                bullet_list.add(bullet)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.changespeed(0, -5)
        # --- Game Logic ---
        num += 1
        if num==31:
            num=0
        player.move(current_room.wall_list)
        for bullet in bullet_list:
            bullet.move(current_room.wall_list, nazi_list)
        for nazi in nazi_list:
            if movingsprites.has(player):
                nazi.move(current_room.wall_list,movingsprites, player.rect.center, nazi_list)
            if nazi.fire() and num==30 and movingsprites.has(player):
                enemybullet = EnemyBullet(nazi.rect.center[0],nazi.rect.center[1],nazi.mousex2,nazi.mousey2)
                enemybullet_list.add(enemybullet)
        for enemybullet in enemybullet_list:
            enemybullet.move(current_room.wall_list, movingsprites)
        if player.rect.y < -0:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.y = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.y = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.y = 790
            for bullet in bullet_list:
                bullet.rect.y = bullet.rect.y+800
            for enemybullet in enemybullet_list:
                enemybullet.rect.y = enemybullet.rect.y+800
            for nazi in nazi_list:
                nazi.rect.y = nazi.rect.y+800
        if player.rect.y > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.y = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.y = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.y = 0
            for bullet in bullet_list:
                bullet.rect.y = bullet.rect.y-800
            for enemybullet in enemybullet_list:
                enemybullet.rect.y = enemybullet.rect.y-800
            for nazi in nazi_list:
                nazi.rect.y = nazi.rect.y-800
        # --- Drawing ---
        screen.fill(BLACK)

        if movingsprites.has(player):
            player.NoobToob(screen, mousex, mousey)
            player.Health(screen)
        for nazi in nazi_list:
            nazi.NoobToob(screen,player.rect.center)
        nazi_list.draw(screen)
        enemybullet_list.draw(screen)
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        if nazi_list.__len__() == 0:
            screen.blit(youWin,[100,400])
        if (movingsprites.has(player) == False):
            screen.blit(youLose,[10,420])
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def reset():
    print("Reset")
def game():
    print("Game")
    main()
def options():
    print("Options")
def menu():
    pygame.init()
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode([450,300])
    clock = pygame.time.Clock()
    x = False
    font = pygame.font.Font(None,60)
    mx = 0
    my = 0
    click = False
    while x == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = True
                pygame.quit
            if event.type == pygame.MOUSEBUTTONUP:
                click = True
        (mx,my) = pygame.mouse.get_pos()
        screen.fill([0,153,0])
        button1 = font.render("New Game", True, (0, 0, 255),)
        button2 = font.render("Continue", True, (0, 0, 255))
        button3 = font.render("Options/Settings", True, (0, 0, 255))
        button4 = font.render("Quit Game", True, (0, 0, 255))
        if mx>0 and mx<215 and my>0 and my<35:
            button1 = font.render("New Game", True, (0, 255, 255))
            if click:
                reset()
                game()
                menu()
        elif mx>0 and mx<190 and my>40 and my<75:
            button2 = font.render("Continue", True, (0, 255, 255))
            if click:
                game()
                menu()
        elif mx>0 and mx<350 and my>80 and my<115:
            button3 = font.render("Options/Settings", True, (0, 255, 255))
            if click:
                options()
        elif mx>0 and mx<220 and my>120 and my<155:
            button4 = font.render("Quit Game", True, (0, 255, 255))
            if click:
                x = True
                pygame.quit()
        click = False
        if x==False:
            screen.blit(button1, [0,0])
            screen.blit(button2, [0,40])
            screen.blit(button3, [0,80])
            screen.blit(button4, [0,120])
        pygame.display.flip()
        clock.tick(25)
    pygame.quit()
menu()

