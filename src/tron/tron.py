'''
Created on Mar 8, 2015

@author: NVP
'''
import pygame
speed = 10
pygame.init()
size = [700,500]
text = ""
screen = pygame.display.set_mode(size)
#screen2 = pygame.image.load('H:\\warploop.gif').convert
pygame.display.set_caption("Tron")
x = False
w = False
while w==False:
    clock = pygame.time.Clock()
    keys = pygame.key.get_pressed()
    Pause = False
    safetyp = 0
    GREEN = (0,255,0)
    RED = (255,0,0)
    BLACK = (0,0,0)
    
    Blockx1 = 500
    Blocky1 = 250
    """[R,D,L,U]"""
    K1 = [False,False,True,False]
    safety1 = [False,True,True,True]
    safetyBack1 = True
    buttonPressed1 = False
    lose1 = False
    """"""""""""""""""""""""""
    Blockx2 = 200
    Blocky2 = 250
    K2 = [True,False,False,False]
    safety2 = [True,True,False,True]
    safetyBack2 = True
    buttonPressed2 = False
    lose2 = False

    screen.fill(BLACK)
    while x == False and Pause==False:
        print("a")
        if True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = True
                    w = True
                    print("quit")
                elif event.type == pygame.KEYDOWN:
                    if(event.key==pygame.K_RIGHT or event.key==pygame.K_DOWN or event.key==pygame.K_LEFT or event.key==pygame.K_UP):
                        buttonPressed1 = True
                    if event.key == pygame.K_RIGHT and safety1[0] and safetyBack1:
                        K1[0] = True
                        K1[1] = False
                        K1[2] = False
                        K1[3] = False
                        safety1[1] = True
                        safety1[3] = True
                        safety1[2] = False
                        safetyBack1 = False
                    elif event.key == pygame.K_DOWN and safety1[1] and safetyBack1:
                        K1[0] = False
                        K1[2] = False
                        K1[3] = False
                        K1[1] = True
                        safety1[0] = True
                        safety1[2] = True
                        safety1[3] = False
                        safetyBack1 = False
                    elif event.key == pygame.K_LEFT and safety1[2] and safetyBack1:
                        K1[0] = False
                        K1[1] = False
                        K1[3] = False
                        K1[2] = True
                        safety1[0] = False
                        safety1[1] = True
                        safety1[3] = True
                        safetyBack1 = False
                    elif event.key == pygame.K_UP and safety1[3] and safetyBack1:
                        K1[0] = False
                        K1[1] = False
                        K1[2] = False
                        K1[3] = True
                        safety1[0] = True
                        safety1[2] = True
                        safety1[1] = False
                        safetyBack1 = False
                    """"""""""""""""""""""""""""""""""""""""""""""""
                    if(event.key==pygame.K_d or event.key==pygame.K_s or event.key==pygame.K_a or event.key==pygame.K_w):
                        buttonPressed2 = True
                    if event.key == pygame.K_d and safety2[0] and safetyBack2:
                        K2[0] = True
                        K2[1] = False
                        K2[2] = False
                        K2[3] = False
                        safety2[1] = True
                        safety2[3] = True
                        safety2[2] = False
                        safetyBack2 = False
                    elif event.key == pygame.K_s and safety2[1] and safetyBack2:
                        K2[0] = False
                        K2[2] = False
                        K2[3] = False
                        K2[1] = True
                        safety2[0] = True
                        safety2[2] = True
                        safety2[3] = False
                        safetyBack2 = False
                    elif event.key == pygame.K_a and safety2[2] and safetyBack2:
                        K2[0] = False
                        K2[1] = False
                        K2[3] = False
                        K2[2] = True
                        safety2[0] = False
                        safety2[1] = True
                        safety2[3] = True
                        safetyBack2 = False
                    elif event.key == pygame.K_w and safety2[3] and safetyBack2:
                        K2[0] = False
                        K2[1] = False
                        K2[2] = False
                        K2[3] = True
                        safety2[0] = True
                        safety2[2] = True
                        safety2[1] = False
                        safetyBack2 = False
                        
                    elif event.key == pygame.K_p:
                        Pause = True
                        safetyp = 0
                #elif event.type == pygame.KEYUP:
                    #pass
            safetyBack1 = True
            safetyBack2 = True

            #print(pygame.transform.average_color(screen))
            print("b")
            print(lose1," ", lose2," ",x)
            print(buttonPressed1," ",buttonPressed2)
            if(not buttonPressed1):
                Blockx1 -= 10 
            elif K1[0]:
                Blockx1 += 10
            elif K1[1]:
                Blocky1 += 10
            elif K1[2]:
                Blockx1 -= 10
            elif K1[3]:
                Blocky1 -= 10
            """"""""""""""""""
            if(not buttonPressed2):
                Blockx2 += 10 
            elif K2[0]:
                Blockx2 += 10
            elif K2[1]:
                Blocky2 += 10
            elif K2[2]:
                Blockx2 -= 10
            elif K2[3]:
                Blocky2 -= 10
                
            if Blockx1<0 or Blockx1>690 or Blocky1<0 or Blocky1>490:
                lose1 = True
                print("wall")
            """"""""""""""""""""""""
            if Blockx2<0 or Blockx2>690 or Blocky2<0 or Blocky2>490:
                lose2 = True
                print("wall")
                
            if(lose1 or lose2):
                x=True
                break
            
            hit1 = pygame.transform.average_color(screen,[Blockx1+1,Blocky1+1,8,8]) == (0,0,0,0)
            hit2 = pygame.transform.average_color(screen,[Blockx2+1,Blocky2+1,8,8]) == (0,0,0,0)
            print(pygame.transform.average_color(screen,[Blockx1+1,Blocky1+1,8,8]))
            print(pygame.transform.average_color(screen,[Blockx2+1,Blocky2+1,8,8]))
            if not(hit1):
                lose1 = True
            else:
                pygame.draw.rect(screen,GREEN,[Blockx1,Blocky1,10,10],0)
            """"""""""""""""""""""""""""""""""""""""""""""""""""""""
            if not(hit2):
                lose2 = True
            else:
                pygame.draw.rect(screen,RED,[Blockx2,Blocky2,10,10],0)
            
            if(Blockx1==Blockx2 and Blocky1==Blocky2):
                lose1 = True
                lose2 = True
            #print(lose1," ", lose2," ",x)
            #pygame.draw.rect(screen,GREEN,[position[counter],position[counter+1],10,10],0)


            pygame.display.flip()

            if lose1 or lose2:
                x = True
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
    if lose1 and lose2:
        text = font.render("YOU BOTH LOST! ......or won!.....or what??", False, (255, 255, 255))
    elif lose1:
        text = font.render("PLAYER 2 WINS!", False, (255, 255, 255))
    elif lose2:
        text = font.render("PLAYER 1 WINS!", False, (255, 255, 255))
    screen.blit(text, [100,200])
    text = font.render("Press 'space' to restart", False, (255, 255, 255))
    screen.blit(text, [195,240])
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