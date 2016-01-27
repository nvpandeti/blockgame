'''
Created on Dec 14, 2013

@author: NVP
'''
import pygame
import random
import math
global size;
size = [900,550]
def drawCube(screen, color, x, y):
    startX = size[0]/2 + (x-y)*5*math.sqrt(3)
    startY = (x+y)*5
    pygame.draw.polygon(screen, (color[0]-100,color[1]-100,color[2]-100), ((startX+5*math.sqrt(3),startY+5), (startX,startY+10), (startX,startY+20), (startX+5*math.sqrt(3),startY+15)), 0)
    pygame.draw.polygon(screen, (color[0]-66,color[1]-66,color[2]-66), ((startX-5*math.sqrt(3),startY+5), (startX-5*math.sqrt(3),startY+15), (startX,startY+20), (startX,startY+10)), 0)
    pygame.draw.polygon(screen, (color[0],color[1],color[2]), ((startX-5*math.sqrt(3),startY+5), (startX,startY+10), (startX+5*math.sqrt(3),startY+5), (startX,startY)), 0)

    
speed = 20   #float(input("How fast do you want to go?(FPS)"))
pygame.init()

text = ""
compass = pygame.image.load('compass.jpg')
#compass = pygame.transform.scale(compass,(50,42))
screen = pygame.display.set_mode(size)
#screen2 = pygame.image.load('H:\\warploop.gif').convert
pygame.display.set_caption("Snake")
x = False
w = False
while w==False:
    clock = pygame.time.Clock()
    Blockx = 4
    Blocky = 4
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
            while(counter<position.__len__()-3):
                if(position[counter]==Blockx and position[counter+1]==Blocky):
                    x = True
                    #print("meep")
                counter=counter+2
#            counter=2
            counter=0
            position.append(Blockx)
            position.append(Blocky)
            #print(position)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = True
                    w = True
                    #uprint("quit")
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
                        boost = 1
                        Colorboost = True
                    elif event.key == pygame.K_p:
                        Pause = True
                        safetyp = 0
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        boost = 0
                        Colorboost = False
            if KR:
                Blockx=Blockx+1+boost
            elif KD:
                Blocky=Blocky+1+boost
            elif KL:
                Blockx=Blockx-1-boost
            elif KU:
                Blocky=Blocky-1-boost
            safetyBack = True
#            if Score==0:
#                screen.fill([0,0,0])
            screen.fill([0,0,0])
            #screen2 = pygame.transform.scale(screen2, (700,500))
            #screen.blit(screen2,[0,0])
            pygame.draw.polygon(screen,[100,100,100],((450,10),(450+250*math.sqrt(3),260),(450,510),(450-250*math.sqrt(3),260)),1)
            if Apple:
                Applex = random.randrange(0,49,1)
                Appley = random.randrange(0,49,1)
                #print(str(Applex)+""+str(Appley))
                Apple = False
            #pygame.draw.rect(screen,[255,0,0],[Applex*10,Appley*10,10,10],0)
            #drawCube(screen,[255,100,0],Applex,Appley)
            sortedPosition = []
            for i in range(position.__len__()):
                sortedPosition.append(position[i])
            sortedPosition.append(Applex)
            sortedPosition.append(Appley)
            for i in range(sortedPosition.__len__()//2-1):
                for j in range(sortedPosition.__len__()//2-1-i):
                    if(sortedPosition[j*2]>sortedPosition[(j+1)*2] or (sortedPosition[j*2]==sortedPosition[(j+1)*2] and sortedPosition[j*2+1]>sortedPosition[(j+1)*2+1])):
                        tempX = sortedPosition[j*2]
                        tempY = sortedPosition[j*2+1]
                        sortedPosition[(j)*2] = sortedPosition[(j+1)*2]
                        sortedPosition[j*2+1] = sortedPosition[(j+1)*2+1]
                        sortedPosition[(j+1)*2] = tempX
                        sortedPosition[(j+1)*2+1] = tempY
            #print(sortedPosition)
            #s = ""
            while(counter<sortedPosition.__len__()-1):
                R = 101
                G = 255
                B = 101
                if Colorboost:
                    R = random.randrange(101,255,1)
                    G = random.randrange(101,255,1)
                    B = random.randrange(101,255,1)
                #pygame.draw.rect(screen,[R,G,B],[position[counter]*10,position[counter+1]*10,10,10],0)
                bla = (sortedPosition[counter]==Applex and sortedPosition[counter+1]==Appley)
                blah = (counter+2<sortedPosition.__len__() and (sortedPosition[counter+2]==Applex and sortedPosition[counter+3]==Appley))
                if(bla and not blah):
                    drawCube(screen,[255,100,100],sortedPosition[counter],sortedPosition[counter+1])
                    #s += "r "+str(sortedPosition[counter])+" "+str(sortedPosition[counter+1])+" "
                    #if(blah):
                    #    counter =counter+2
                else:
                    drawCube(screen,[R,G,B],sortedPosition[counter],sortedPosition[counter+1])
                    #s += "g "+str(sortedPosition[counter])+" "+str(sortedPosition[counter+1])+" "
                
                counter=counter+2
            #print(s)

#             R = 0
#             G = 255
#             B = 0
#             if Colorboost:
#                 R = random.randrange(1,255,1)
#                 G = random.randrange(1,255,1)
#                 B = random.randrange(1,255,1)
#             pygame.draw.rect(screen,[0,0,0],[0,0,40,10],0)
#             pygame.draw.rect(screen,[0,0,0],[position[0],position[1],10,10],0)
#             pygame.draw.rect(screen,[R,G,B],[position[position.__len__()-2],position[position.__len__()-1],10,10],0)
            counter=0
            #for i in range(0,500,10):
            #    pygame.draw.line(screen,[0,0,0],[0,i],[700,i],1)
            #for j in range(0,700,10):
            #    pygame.draw.line(screen,[0,0,0],[j,0],[j,500],1)
            font = pygame.font.Font(None, 30)
            text = font.render("Score: "+str(Score), False, (255, 255, 255))
            screen.blit(text, [0,0])
            screen.blit(compass,[0,20])
            pygame.display.flip()
            if Blockx<0 or Blockx>49 or Blocky<0 or Blocky>49:
                x = True
                #print("wall")
            if Applex==Blockx and Appley==Blocky:
                Apple = True
                position.append(700)
                position.append(500)
                position.append(710)
                position.append(510)
                position.append(720)
                position.append(520)
                position.append(730)
                position.append(530)
                position.append(Blockx)
                position.append(Blocky)
#                 if Score==0:
#                     screen.fill([0,0,0])
                Score=Score+20
            position.pop(0)
            position.pop(0)
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

