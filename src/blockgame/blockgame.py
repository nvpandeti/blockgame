'''
Created on Dec 9, 2013

@author: NVP
'''
import pygame
import random
print("Objective: Reach the red dot before the timer runs out.")
print("           Your score and the timer are in the top left corner.")
print("Controls: Arrow keys to move")
print("          Space to boost")
print("          't' to teleport")
print("          'p' to pause")
difficulty = float(input("What difficulty would you like? (1-10, 1 being the hardest)"))
pygame.init()
size = [700,500]
screen = pygame.display.set_mode(size)
screen2 = pygame.image.load('C:\\Users\\NVP\\Pictures\\2011-07-28 001\\IMG_0589.JPG').convert()
pygame.display.set_caption("Blockgame")
x = False
clock = pygame.time.Clock()
a = 40
b = 40
c = 350
d = 250
keys = pygame.key.get_pressed()
KR = False
KD = False
KL = False
KU = False
Apple = True
Score = 0
Timer = 1000
boost = 0
fps = 120-(difficulty-1)*10
Pause = False
while x == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if Pause == False:
                    Pause = True
                elif Pause:
                    Pause = False
            elif Pause == False:
                if event.key == pygame.K_RIGHT:
                    KR = True
                elif event.key == pygame.K_DOWN:
                    KD = True
                elif event.key == pygame.K_LEFT:
                    KL = True
                elif event.key == pygame.K_UP:
                    KU = True
                elif event.key == pygame.K_SPACE:
                    boost = 6
                elif event.key == pygame.K_t:
                    a = random.randint(c-55,c+45)
                    b = random.randint(d-55,d+45)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                KR = False
            elif event.key == pygame.K_DOWN:
                KD = False
            elif event.key == pygame.K_LEFT:
                KL = False
            elif event.key == pygame.K_UP:
                KU = False
            elif event.key == pygame.K_SPACE:
                boost = 0
    if KR and a<=676:
        a=a+4+boost
    elif KD and b<=476:
        b=b+4+boost
    elif KL and a>=4:
        a=a-4-boost
    elif KU and b>=4:
        b=b-4-boost
    screen.fill([0,0,0])
    screen2 = pygame.transform.scale(screen2, (700,500))
    screen.blit(screen2,[0,0])
    if Apple:
        c = random.randint(0,690)
        d = random.randint(0,490)
        Apple = False
    pygame.draw.rect(screen,[255,0,0],[c,d,10,10],0)
    pygame.draw.rect(screen,[0,255,0],[a,b,20,20],0)
    if KR:
        pygame.draw.lines(screen,[0,255,0],True,[(a+20,b-10),(a+20,b+30),(a+30,b+10)],6)
    elif KD:
        pygame.draw.lines(screen,[0,255,0],True,[(a-10,b+20),(a+30,b+20),(a+10,b+30)],6)
    elif KL:
        pygame.draw.lines(screen,[0,255,0],True,[(a+0,b-10),(a+0,b+30),(a-10,b+10)],6)
    elif KU:
        pygame.draw.lines(screen,[0,255,0],True,[(a-10,b-0),(a+30,b+0),(a+10,b-10)],6)
    font = pygame.font.Font(None, 18)
    text = font.render(str(Score), True, (255, 255, 255))
    screen.blit(text, [0,0])
    text = font.render(str(Timer), True, (255,255,255))
    screen.blit(text, [0,10])
    pygame.display.flip()
    #if a==2 or a==678 or b==2 or b==478:
        #x = True
    if c<=a+10 and c>=a and d<=b+10 and d>=b:
        Apple = True
        Score=Score+1
        Timer = 500
    if Pause == False:
        Timer=Timer-1
    if Timer==0:
        x = True
    clock.tick(fps)
print("GAME OVER!")
print("Your score was "+str(Score))
pygame.quit()