'''
Created on Jan 3, 2014

@author: NVP
'''
'''
Created on Jan 2, 2014

@author: NVP
'''
import pygame
pygame.init()
screen = pygame.display.set_mode([400,600])
clock = pygame.time.Clock()
x = False
font = pygame.font.Font(None,45)
x1 = 165
y1 = 590
x2 = 165
y2 = 0
xb = 200
yb = 300
movx = 0
movy = 10
R1 = False
L1 = False
Score1 = 0
Score2 = 0
while x == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                R1 = True
            elif event.key == pygame.K_LEFT:
                L1 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                R1 = False
            elif event.key == pygame.K_LEFT:
                L1 = False
    if R1 and x1<=320:
        x1 = x1+10
    if L1 and x1>=0:
        x1 = x1-10
    if x2<xb-35 and x2<=320:
        x2 = x2+7
    if x2>xb-35 and x2>=0:
        x2 = x2-7
    if yb==580:
        movy=-(movy)
        if xb>=x1-10 and xb<=x1+80:
            movx=((xb-x1)-35)/3
        else:
            movx=0
            xb=200
            yb=300
            Score2=Score2+1
    if yb==10:
        movy=-(movy)
        if xb>=x2-10 and xb<=x2+80:
            movx=((xb-x2)-35)/3
        else:
            movx=0
            xb=200
            yb=300
            Score1=Score1+1
    if xb<=0 or xb>=390:
        movx=-(movx)
    xb=xb+movx
    yb=yb+movy
    print(str(xb)+" "+str(yb))
    screen.fill([0,0,0])
    pygame.draw.rect(screen,[255,255,255],[xb,yb,10,10],0)
    pygame.draw.rect(screen,[255,255,255],[x1,y1,80,10],0)
    pygame.draw.rect(screen,[255,255,255],[x2,y2,80,10],0)
    pygame.draw.line(screen,[255,255,255],[0,300],[400,300],1)
    text1 = font.render(str(Score2), True, (255, 255, 255))
    screen.blit(text1, [0,270])
    text2 = font.render(str(Score1), True, (255, 255, 255))
    screen.blit(text2, [0,305])
    pygame.display.flip()
    clock.tick(30)
pygame.quit()