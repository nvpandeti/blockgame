'''
Created on Mar 15, 2014

@author: NVP
'''
import pygame
import random
speed = 20#float(input("How fast do you want to go?(FPS)"))
pygame.init()
length = 400
width = 400
size = [length,width]
text = ""
screen = pygame.display.set_mode(size)
#screen2 = pygame.image.load('H:\\warploop.gif').convert
pygame.display.set_caption("Snake")
x = False
w = False
while w==False:
    clock = pygame.time.Clock()
    Blockx = 40
    Blocky = 40
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
    Colorboost = False
    Pause = False
    safetyp = 0
    safetyBack = True
    R = 0
    G = 0
    B = 0
    Score = 0
    boost = 0
    position = []
    counter = 0
    screen.fill([0,0,0])
    while x == False and Pause==False:
        if Pause==False:
            while(counter<position.__len__()-1):
                if(position[counter]==Blockx and position[counter+1]==Blocky):
                    x = True
                    print("meep")
                counter=counter+2
            counter=0
            position.append(Blockx)
            position.append(Blocky)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = True
                    w = True
                    print("quit")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and safetyR and safetyBack:
                        KR = True
                        KD = False
                        KL = False
                        KU = False
                        safetyD = True
                        safetyL = False
                        safetyU = True
                        safetyBack = False
                    elif event.key == pygame.K_DOWN and safetyD and safetyBack:
                        KR = False
                        KD = True
                        KL = False
                        KU = False
                        safetyR = True
                        safetyL = True
                        safetyU = False
                        safetyBack = False
                    elif event.key == pygame.K_LEFT and safetyL and safetyBack:
                        KR = False
                        KD = False
                        KL = True
                        KU = False
                        safetyR = False
                        safetyD = True
                        safetyU = True
                        safetyBack = False
                    elif event.key == pygame.K_UP and safetyU and safetyBack:
                        KR = False
                        KD = False
                        KL = False
                        KU = True
                        safetyR = True
                        safetyD = False
                        safetyL = True
                        safetyBack = False
                    elif event.key == pygame.K_SPACE:
                        boost = 10
                        Colorboost = True
                    elif event.key == pygame.K_p:
                        Pause = True
                        safetyp = 0
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        boost = 0
                        Colorboost = False
            if KR:
                Blockx=Blockx+10+boost
            elif KD:
                Blocky=Blocky+10+boost
            elif KL:
                Blockx=Blockx-10-boost
            elif KU:
                Blocky=Blocky-10-boost
            safetyBack = True
            screen.fill([0,0,0])
            #screen2 = pygame.transform.scale(screen2, (700,500))
            #screen.blit(screen2,[0,0])
            if Apple:
                Applex = random.randrange(0,length-10,10)
                Appley = random.randrange(0,width-10,10)
                Apple = False
                for a in range(0,position.__len__(),2):
                    if Applex==position[a] and Appley==position[a+1]:
                        Apple=True
            pygame.draw.rect(screen,[255,0,0],[Applex,Appley,10,10],0)
            while(counter<position.__len__()-1):
                R = 0
                G = 255
                B = 0
                if Colorboost:
                    R = random.randrange(1,255,1)
                    G = random.randrange(1,255,1)
                    B = random.randrange(1,255,1)
                pygame.draw.rect(screen,[R,G,B],[position[counter],position[counter+1],10,10],0)
                counter=counter+2
            counter=0
            font = pygame.font.Font(None, 18)
            text = font.render(str(Score), False, (255, 255, 255))
            screen.blit(text, [0,0])
            pygame.display.flip()
            if Blockx<0 or Blockx>length-10 or Blocky<0 or Blocky>width-10:
                x = True
                print("wall")
            if Applex==Blockx and Appley==Blocky:
                Apple = True
                position.append(Blockx)
                position.append(Blocky)
                Score=Score+20
            position.pop()
            position.pop()
            clock.tick(speed)
        while Pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and safetyp==1:
                        Pause = False
                        safetyp = 0
                    safetyp=1
                if event.type == pygame.QUIT:
                    Pause = False
                    x = True
                    w = True
    print("GAME OVER!")
    font = pygame.font.Font(None, 40)
    text = font.render("GAME OVER!", False, (255, 255, 255))
    screen.blit(text, [340,200])
    print("Your score was "+str(Score))
    text = font.render("Your score was "+str(Score), False, (255, 255, 255))
    screen.blit(text, [320,220])
    text = font.render("Press 'space' to restart", False, (255, 255, 255))
    screen.blit(text, [295,240])
    pygame.display.flip()
    while x==True:
        if w==True:
            break
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x=False
            if event.type == pygame.QUIT:
                w = True
    while Pause:
        for event in pygame.event.get():
            if event.key == pygame.K_p and safetyp==1:
                Pause = False
                safetyp = 0
            safetyp=1
pygame.quit()