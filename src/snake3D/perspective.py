'''
Created on Jan 17, 2016

@author: NVP
'''

import pygame
#import random
import math
class Face:
    def __init__(self, corner1, corner2, corner3, corner4, num):
        self.corners = [corner1, corner2, corner3, corner4]
        self.num = num
        xSum = 0
        ySum = 0
        zSum = 0
        for corner in self.corners:
            xSum += corner[0]
            ySum += corner[1]
            zSum += corner[2]
        
        self.center = (xSum/4, ySum/4, zSum/4)
        print(self.center)
global size;
size = [900,550]
speed = 20   #float(input("How fast do you want to go?(FPS)"))
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")
x = False

clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
screen.fill([0,0,0])
posH = 0
posZ = 45
r = 4
cube = ((1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1))
faces = [Face(cube[0],cube[1],cube[3],cube[2],0),
         Face(cube[0],cube[1],cube[5],cube[4],1),
         Face(cube[4],cube[5],cube[7],cube[6],2),
         Face(cube[6],cube[7],cube[3],cube[2],3),
         Face(cube[6],cube[4],cube[0],cube[2],4),
         Face(cube[7],cube[5],cube[1],cube[3],5)]

while x == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
            #uprint("quit")
    
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT] == 1:
        posH+=1
        if posH>=360:
            posH=0
    if keyboard[pygame.K_RIGHT] == 1:
        posH-=1
        if posH<0:
            posH=359
    if keyboard[pygame.K_DOWN] == 1 and posZ>-90:
        posZ-=1
    if keyboard[pygame.K_UP] == 1 and posZ<90:
        posZ+=1
    
    screen.fill([0,0,0])
    realX = r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    realY = r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
    realZ = r * math.sin(math.radians(posZ))
    
    for i in range(faces.__len__()-1):
        sorted = False
        for j in range(faces.__len__()-1-i):
            if(math.sqrt((realX - faces[j].center[0])**2 + (realY - faces[j].center[1])**2 + (realZ - faces[j].center[2])**2)
               < math.sqrt((realX - faces[j+1].center[0])**2 + (realY - faces[j+1].center[1])**2 + (realZ - faces[j+1].center[2])**2)):
                temp = faces[j]
                faces[j] = faces[j+1]
                faces[j+1] = temp
                sorted = True
        if(sorted):
            break
        
    for face in faces:
        
        angleD = []
        
        for corner in face.corners:
            #"""
            v1mag = math.sqrt((0-realX)**2 + (0-realY)**2 + (0-realZ)**2)
            v2mag = math.sqrt( (corner[0]-realX)**2 + (corner[1]-realY)**2 + (corner[2]-realZ)**2 )
            
            v1norm = [(0-realX) / v1mag, (0-realY) / v1mag, (0-realZ) / v1mag]
            v2norm = [(corner[0]-realX) / v2mag, (corner[1]-realY) / v2mag, (corner[2]-realZ) / v2mag]
            
            angleD.append( math.degrees( math.acos( v1norm[0] * v2norm[0] + v1norm[1] * v2norm[1] + v1norm[2] * v2norm[2] ) ) )
            #"""
            
            angleD.append( math.degrees( math.acos( ( (0 - realX)*(corner[0] - realX) + (0 - realY)*(corner[1] - realY) + (0 - realZ)*(corner[2] - realZ) ) / ( math.sqrt( math.pow( 0 - realX, 2) + math.pow( 0 - realY, 2) + math.pow( 0 - realZ, 2) ) *  math.sqrt( math.pow( corner[0] - realX, 2) + math.pow( corner[1] - realY, 2) + math.pow( corner[2] - realZ, 2) ) ) ) ) )
        #print(angleD)
        #"""
        angleH = []
        angleV = []
        for corner in face.corners:
            angleH.append( math.degrees( math.atan2(corner[1] - realY, corner[0] - realX) - math.atan2(0 - realY, 0 - realX)))
            angleV.append( math.degrees( math.atan2(corner[2] - realZ, corner[0] - realX) - math.atan2(0 - realZ, 0 - realX)))
        #pygame.draw.circle(screen,(0,255,0),(int(450+angleH[0]*5), int(275-angleV[0]*5)),3,0)
        #pygame.draw.circle(screen,(0,255,0),(int(450+angleH[1]*5), int(275-angleV[1]*5)),3,0)
        #pygame.draw.circle(screen,(0,255,0),(int(450+angleH[2]*5), int(275-angleV[2]*5)),3,0)
        #pygame.draw.circle(screen,(0,255,0),(int(450+angleH[3]*5), int(275-angleV[3]*5)),3,0)
        
        pygame.draw.polygon(screen, (0,255,0), ((450+angleH[0]*5, 275-angleV[0]*5), (450+angleH[1]*5, 275-angleV[1]*5), (450+angleH[2]*5, 275-angleV[2]*5), (450+angleH[3]*5, 275-angleV[3]*5)), 0)
        pygame.draw.polygon(screen, (0,0,0), ((450+angleH[0]*5, 275-angleV[0]*5), (450+angleH[1]*5, 275-angleV[1]*5), (450+angleH[2]*5, 275-angleV[2]*5), (450+angleH[3]*5, 275-angleV[3]*5)), 1)
        #"""
        #break
    pygame.draw.circle(screen, (0,0,0),(450,275),3,0)
    
    font = pygame.font.Font(None, 40)
    text = font.render(str(realX), False, (255, 255, 255))
    screen.blit(text, [0,0])
    text = font.render(str(realY), False, (255, 255, 255))
    screen.blit(text, [0,30])
    text = font.render(str(realZ), False, (255, 255, 255))
    screen.blit(text, [0,60])
    
    text = font.render(str(faces[0].num), False, (255, 255, 255))
    screen.blit(text, [300,0])
    text = font.render(str(faces[1].num), False, (255, 255, 255))
    screen.blit(text, [320,0])
    text = font.render(str(faces[2].num), False, (255, 255, 255))
    screen.blit(text, [340,0])
    text = font.render(str(faces[3].num), False, (255, 255, 255))
    screen.blit(text, [360,0])
    text = font.render(str(faces[4].num), False, (255, 255, 255))
    screen.blit(text, [380,0])
    text = font.render(str(faces[5].num), False, (255, 255, 255))
    screen.blit(text, [400,0])
    
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()