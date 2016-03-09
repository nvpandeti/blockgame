'''
Created on Dec 26, 2013

@author: NVP
'''
import pygame
import random
speed = 20#float(input("How fast do you want to go?(FPS)"))
pygame.init()
size = [659,439]
screen = pygame.display.set_mode(size)
#screen2 = pygame.image.load('C:\\Users\\NVP\\Pictures\\2011-07-28 001\\IMG_0589.JPG')
pygame.display.set_caption("Blockgame")
x = False
clock = pygame.time.Clock()
Blockx = 44
Blocky = 44
Chasex = 330
Chasey = 220
keys = pygame.key.get_pressed()
KR = False
KD = False
KL = False
KU = False
safetyR = True
safetyD = True
safetyL = True
safetyU = True
Apple = True
Score = 0
boost = 0
position = []
counter = 0
while x == False:
    while(counter<position.__len__()-3):
        if(position[counter]==Blockx and position[counter+1]==Blocky):
            x = True
        counter=counter+2
    counter=0
    position.append(Blockx)
    position.append(Blocky)
    while(counter<position.__len__()):
        if(position[counter]+10>=Chasex and position[counter]-10<=Chasex and position[counter+1]+10>=Chasey and position[counter+1]-10<=Chasey):
            x = True
        counter=counter+2
    counter=0
    #print(position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and safetyR:
                KR = True
                KD = False
                KL = False
                KU = False
                safetyD = True
                safetyL = False
                safetyU = True
            elif event.key == pygame.K_DOWN and safetyD:
                KR = False
                KD = True
                KL = False
                KU = False
                safetyR = True
                safetyL = True
                safetyU = False
            elif event.key == pygame.K_LEFT and safetyL:
                KR = False
                KD = False
                KL = True
                KU = False
                safetyR = False
                safetyD = True
                safetyU = True
            elif event.key == pygame.K_UP and safetyU:
                KR = False
                KD = False
                KL = False
                KU = True
                safetyR = True
                safetyD = False
                safetyL = True
            elif event.key == pygame.K_SPACE:
                boost = 11
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                boost = 0
    if KR:
        Blockx=Blockx+11+boost
    elif KD:
        Blocky=Blocky+11+boost
    elif KL:
        Blockx=Blockx-11-boost
    elif KU:
        Blocky=Blocky-11-boost
    if Chasex<Blockx:
        Chasex=Chasex+2
    elif Chasex>Blockx:
        Chasex=Chasex-2
    if Chasey<Blocky:
        Chasey=Chasey+2
    elif Chasey>Blocky:
        Chasey=Chasey-2
    screen.fill([0,0,0])
    #screen2 = pygame.transform.scale(screen2, (700,500))
    #screen.blit(screen2,[0,0])
    if Apple:
        Applex = random.randrange(0,649,11)
        Appley = random.randrange(0,429,11)
        #print(str(Applex)+""+str(Appley))
        Apple = False
    pygame.draw.rect(screen,[255,0,0],[Applex,Appley,10,10],0)
    while(counter<position.__len__()-1):
        pygame.draw.rect(screen,[0,255,0],[position[counter],position[counter+1],10,10],0)
        counter=counter+2
    counter=0
    pygame.draw.rect(screen,[0,0,225],[Chasex,Chasey,10,10],0)
    font = pygame.font.Font(None, 18)
    text = font.render(str(Score), False, (255, 255, 255))
    screen.blit(text, [0,0])
    pygame.display.flip()
    if Blockx<0 or Blockx>659 or Blocky<0 or Blocky>439:
        x = True
    if Applex==Blockx and Appley==Blocky:
        Apple = True
        Score=Score+1
        position.append(Blockx)
        position.append(Blocky)
    position.pop(0)
    position.pop(0)
    clock.tick(speed)
print("GAME OVER!")
print("Your score was "+str(Score))
pygame.quit()