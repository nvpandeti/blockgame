'''
Created on Jan 17, 2016

@author: NVP
'''

import pygame
#import random
import math
class Face:
    def __init__(self, *args):
        self.corners = args
        #self.num = num
        xSum = 0
        ySum = 0
        zSum = 0
        for corner in self.corners:
            xSum += corner[0]
            ySum += corner[1]
            zSum += corner[2]
        
        self.center = (xSum/self.corners.__len__(), ySum/self.corners.__len__(), zSum/self.corners.__len__())
        #print(self.center)
class Cube:
    def __init__(self, x, y, z, length, width, height):
        self.cube = ((x+length,y+width,z+height), (x+length,y+width,z), (x+length,y,z+height), (x+length,y,z), (x,y+width,z+height), (x,y+width,z), (x,y,z+height), (x,y,z))
        self.faces = [Face(self.cube[0],self.cube[1],self.cube[3],self.cube[2]),
                      Face(self.cube[0],self.cube[1],self.cube[5],self.cube[4]),
                      Face(self.cube[4],self.cube[5],self.cube[7],self.cube[6]),
                      Face(self.cube[6],self.cube[7],self.cube[3],self.cube[2]),
                      Face(self.cube[6],self.cube[4],self.cube[0],self.cube[2]),
                      Face(self.cube[7],self.cube[5],self.cube[1],self.cube[3])]
        
class SquarePyramid:
    def __init__(self, x, y, z, length, width, height):
        self.sqPy = ((x,y+width,z), (x+length,y+width,z), (x+length,y,z), (x,y,z), (x+length/2, y+width/2, z+height))
        self.faces = [Face(self.sqPy[0],self.sqPy[1],self.sqPy[2],self.sqPy[3]),
                      Face(self.sqPy[0],self.sqPy[1],self.sqPy[4]),
                      Face(self.sqPy[1],self.sqPy[2],self.sqPy[4]),
                      Face(self.sqPy[2],self.sqPy[3],self.sqPy[4]),
                      Face(self.sqPy[3],self.sqPy[0],self.sqPy[4])]

class Sphere:
    def __init__(self, x, y, z, r, quality):
        self.sphere = []
        posH = 0
        posZ = 90
        changeH = 360/quality
        changeZ = 180/quality
        self.sphere.append((x,y,z+r))
        posZ += changeZ
        for i in range(quality-2):
            for j in range(quality):
                self.sphere.append((x + r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    y + r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    z + r * math.sin(math.radians(posZ))))
                posH += changeH
            posH=0
            posZ = changeZ
        self.sphere.append((x,y,z-r))
        
        self.faces = []
        
        
        
        
        
global size;
size = [900,550]
speed = 50   #float(input("How fast do you want to go?(FPS)"))
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Perspective")
x = False

clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
screen.fill([0,0,0])
posH = 0
posZ = 45

realX = 7
realY = 0
realZ = 7
origin = [0,0,0]
r = 10
"""
cube = ((1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1))
faces = [Face(cube[0],cube[1],cube[3],cube[2],0),
         Face(cube[0],cube[1],cube[5],cube[4],1),
         Face(cube[4],cube[5],cube[7],cube[6],2),
         Face(cube[6],cube[7],cube[3],cube[2],3),
         Face(cube[6],cube[4],cube[0],cube[2],4),
         Face(cube[7],cube[5],cube[1],cube[3],5)]
"""
shapes = []
shapes.append(SquarePyramid(-100,-100,-100,90,90,50))
#"""
shapes.append(Cube(-1,-1,-1,2,2,2))
shapes.append(Cube(-3,-1,-1,2,2,2))
shapes.append(Cube(1,-1,-1,2,2,2))
shapes.append(Cube(3,-1,-1,2,2,2))
shapes.append(Cube(3,-1,1,2,2,2))
shapes.append(Cube(3,-1,3,2,2,2))
shapes.append(Cube(3,-1,-3,2,2,2))
shapes.append(Cube(3,-1,-5,2,2,2))
shapes.append(Cube(-3,-1,1,2,2,2))
shapes.append(Cube(-3,-1,3,2,2,2))
shapes.append(Cube(-3,-1,-3,2,2,2))
shapes.append(Cube(-3,-1,-5,2,2,2))
shapes.append(Cube(7,-1,1,2,2,2))
shapes.append(Cube(7,-1,-3,2,2,2))
shapes.append(Cube(7,-1,-5,2,2,2))
#"""
while x == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
            #uprint("quit")
    
    keyboard = pygame.key.get_pressed()
    
    if keyboard[pygame.K_LEFT] == 1:
        posH-=3
        if posH<0:
            posH=359
    if keyboard[pygame.K_RIGHT] == 1:
        posH+=3
        if posH>=360:
            posH=0
    if keyboard[pygame.K_DOWN] == 1 and posZ>-89:
        posZ-=2
    if keyboard[pygame.K_UP] == 1 and posZ<89:
        posZ+=2
    if keyboard[pygame.K_w] == 1:
        realX += .5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += .5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realZ += .5 * math.sin(math.radians(posZ))
    if keyboard[pygame.K_s] == 1:
        realX += -.5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += -.5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realZ += -.5 * math.sin(math.radians(posZ))
    if keyboard[pygame.K_a] == 1:
        realX += .5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += -.5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    if keyboard[pygame.K_d] == 1:
        realX += -.5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += .5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    if keyboard[pygame.K_q] == 1:
        realX += -.5 * math.cos(math.radians(posH)) * math.sin(math.radians(posZ))
        realY += -.5 * math.sin(math.radians(posH)) * math.sin(math.radians(posZ))
        realZ += -math.sqrt((.5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (.5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)))**2)
    if keyboard[pygame.K_2] == 1:
        realX += .5 * math.cos(math.radians(posH)) * math.sin(math.radians(posZ))
        realY += .5 * math.sin(math.radians(posH)) * math.sin(math.radians(posZ))
        realZ += math.sqrt((.5 * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (.5 * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)))**2)
        
    origin[0] = realX + r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    origin[1] = realY + r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
    origin[2] = realZ + r * math.sin(math.radians(posZ))
    """
    if keyboard[pygame.K_LEFT] == 1:
        posH+=1
        if posH>=360:
            posH=0
    if keyboard[pygame.K_RIGHT] == 1:
        posH-=1
        if posH<0:
            posH=359
    if keyboard[pygame.K_DOWN] == 1 and posZ>-89:
        posZ-=1
    if keyboard[pygame.K_UP] == 1 and posZ<89:
        posZ+=1
    
    
    realX = r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    realY = r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
    realZ = r * math.sin(math.radians(posZ))
    """
    faces = []
    for s in shapes:
        for face in s.faces:
            faces.append(face)
    
    
    for i in range(faces.__len__()-1):
        sorted = True
        for j in range(faces.__len__()-1-i):
            if(math.sqrt((realX - faces[j].center[0])**2 + (realY - faces[j].center[1])**2 + (realZ - faces[j].center[2])**2)
               < math.sqrt((realX - faces[j+1].center[0])**2 + (realY - faces[j+1].center[1])**2 + (realZ - faces[j+1].center[2])**2)):
                temp = faces[j]
                faces[j] = faces[j+1]
                faces[j+1] = temp
                sorted = False
        if(sorted):
            break
        
    screen.fill([0,0,0])
    for face in faces:
        
        angleD = []
        angleR = []
        for corner in face.corners:
            """
            v1mag = math.sqrt((0-realX)**2 + (0-realY)**2 + (0-realZ)**2)
            v2mag = math.sqrt( (corner[0]-realX)**2 + (corner[1]-realY)**2 + (corner[2]-realZ)**2 )
            
            v1norm = [(0-realX) / v1mag, (0-realY) / v1mag, (0-realZ) / v1mag]
            v2norm = [(corner[0]-realX) / v2mag, (corner[1]-realY) / v2mag, (corner[2]-realZ) / v2mag]
            
            angleD.append( math.degrees( math.acos( v1norm[0] * v2norm[0] + v1norm[1] * v2norm[1] + v1norm[2] * v2norm[2] ) ) )
            """
            
            angleD.append( math.degrees( math.acos( ( (origin[0] - realX)*(corner[0] - realX) + (origin[1] - realY)*(corner[1] - realY) + (origin[2] - realZ)*(corner[2] - realZ) ) 
                                                    / ( math.sqrt( ( origin[0] - realX)**2 + ( origin[1] - realY)**2 + ( origin[2] - realZ)**2 ) *  math.sqrt( ( corner[0] - realX)**2 + ( corner[1] - realY)**2 + ( corner[2] - realZ)**2 ) ) ) ) )
            
            t = - ( (origin[0] - realX)*(realX - corner[0]) + (origin[1] - realY)*(realY - corner[1]) + (origin[2] - realZ)*(realZ - corner[2]) ) / ( (origin[0] - realX)**2 + (origin[1] - realY)**2 + (origin[2] - realZ)**2 )
            vertex = [realX + (origin[0] - realX)*t, realY + (origin[1] - realY)*t, realZ + (origin[2] - realZ)*t]
            perpendicular = [vertex[0] - (origin[1] - realY), vertex[1] + (origin[0] - realX), vertex[2]]
            R = math.acos( ( (perpendicular[0] - vertex[0])*(corner[0] - vertex[0]) + (perpendicular[1] - vertex[1])*(corner[1] - vertex[1]) + (perpendicular[2] - vertex[2])*(corner[2] - vertex[2]) ) 
                           / ( math.sqrt( ( perpendicular[0] - vertex[0])**2 + ( perpendicular[1] - vertex[1])**2 + ( perpendicular[2] - vertex[2])**2 ) *  math.sqrt( ( corner[0] - vertex[0])**2 + ( corner[1] - vertex[1])**2 + ( corner[2] - vertex[2])**2 ) ) )
            if(corner[2]<perpendicular[2]):
                angleR.append(2*math.pi - R)
            else:
                angleR.append(R)
            
        #print(angleD)
        points = []
        for i in range(face.corners.__len__()):
            points.append((450+angleD[i]*15*math.cos(angleR[i]), 275-angleD[i]*15*math.sin(angleR[i])))
        pygame.draw.polygon(screen, (0,255,0), points, 0)
        pygame.draw.polygon(screen, (0,0,0), points, 1)
        #pygame.draw.circle(screen,(0,255,0),(int(450+angleD[0]*5*math.cos(angleR[0])), int(275-angleD[0]*5*math.sin(angleR[0]))),3,0)
        
        """
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
        """
        #break
    pygame.draw.circle(screen, (0,0,0),(450,275),3,0)
    
    font = pygame.font.Font(None, 40)
    text = font.render(str(realX), False, (255, 255, 255))
    screen.blit(text, [0,0])
    text = font.render(str(realY), False, (255, 255, 255))
    screen.blit(text, [0,30])
    text = font.render(str(realZ), False, (255, 255, 255))
    screen.blit(text, [0,60])
    
    text = font.render(str(origin[0]), False, (255, 255, 255))
    screen.blit(text, [0,120])
    text = font.render(str(origin[1]), False, (255, 255, 255))
    screen.blit(text, [0,150])
    text = font.render(str(origin[2]), False, (255, 255, 255))
    screen.blit(text, [0,180])
    """
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
    """
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()