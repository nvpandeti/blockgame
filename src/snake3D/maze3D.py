'''
Created on Mar 15, 2016

@author: Nitu
'''


import pygame
import random
import math
from random import choice

class Face:
    def __init__(self, color, *args):
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
        
        self.color = color
        
        a = (self.corners[1][0] - self.corners[0][0], self.corners[1][1] - self.corners[0][1], self.corners[1][2] - self.corners[0][2])
        b = (self.corners[2][0] - self.corners[0][0], self.corners[2][1] - self.corners[0][1], self.corners[2][2] - self.corners[0][2])
        
        self.normal = ( self.center[0] + (a[1]*b[2] - a[2]*b[1]),
                        self.center[1] + (a[2]*b[0] - a[0]*b[2]),
                        self.center[2] + (a[0]*b[1] - a[1]*b[0]) )
        #print(self.center)
    def __mul__(self, other):
        return (self.color[0]*other, self.color[1]*other, self.color[2]*other)
    def __rmul__(self, other):
        return (self.color[0]*other, self.color[1]*other, self.color[2]*other)
    def getDist(self, realX, realY, realZ):
        return math.sqrt((realX - self.center[0])**2 + (realY - self.center[1])**2 + (realZ - self.center[2])**2)
    
        
class Cube:
    def __init__(self, color, x, y, z, length, width, height):
        self.cube = ((x+length,y+width,z+height), (x+length,y+width,z), (x+length,y,z+height), (x+length,y,z), (x,y+width,z+height), (x,y+width,z), (x,y,z+height), (x,y,z))
        self.faces = [Face(color, self.cube[0],self.cube[1],self.cube[3],self.cube[2]),
                      Face(color, self.cube[0],self.cube[4],self.cube[5],self.cube[1]),
                      Face(color, self.cube[4],self.cube[6],self.cube[7],self.cube[5]),
                      Face(color, self.cube[6],self.cube[2],self.cube[3],self.cube[7]),
                      Face(color, self.cube[6],self.cube[4],self.cube[0],self.cube[2]),
                      Face(color, self.cube[7],self.cube[3],self.cube[1],self.cube[5])]
        
class SquarePyramid:
    def __init__(self, color, x, y, z, length, width, height):
        self.sqPy = ((x,y+width,z), (x+length,y+width,z), (x+length,y,z), (x,y,z), (x+length/2, y+width/2, z+height))
        self.faces = [Face(color, self.sqPy[0],self.sqPy[3],self.sqPy[2],self.sqPy[1]),
                      Face(color, self.sqPy[0],self.sqPy[1],self.sqPy[4]),
                      Face(color, self.sqPy[1],self.sqPy[2],self.sqPy[4]),
                      Face(color, self.sqPy[2],self.sqPy[3],self.sqPy[4]),
                      Face(color, self.sqPy[3],self.sqPy[0],self.sqPy[4])]

class Sphere:
    def __init__(self, color, x, y, z, r, quality):
        self.sphere = []
        posH = 0
        posZ = 90
        changeH = 360/quality
        changeZ = 180/(quality+1)
        self.sphere.append((x,y,z+r))
        posZ += changeZ
        for i in range(quality):
            for j in range(quality):
                self.sphere.append((x + r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    y + r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    z + r * math.sin(math.radians(posZ))))
                posH += changeH
            posH=0
            posZ += changeZ
        self.sphere.append((x,y,z-r))
        
        self.faces = []
        for i in range(quality-1):
            self.faces.append(Face(color, self.sphere[0], self.sphere[i+2], self.sphere[i+1]))
        self.faces.append(Face(color, self.sphere[0], self.sphere[1], self.sphere[quality]))
        for i in range(quality-1):
            for j in range(quality-1):
                self.faces.append(Face(color, self.sphere[i*quality+j+1], self.sphere[i*quality+j+2], self.sphere[(i+1)*quality+j+2], self.sphere[(i+1)*quality+j+1]))
            self.faces.append(Face(color, self.sphere[(i+1)*quality], self.sphere[i*quality+1], self.sphere[(i+1)*quality+1], self.sphere[(i+2)*quality]))
        for i in range(quality-1):
            self.faces.append(Face(color, self.sphere[(quality-1)*quality+i+1], self.sphere[(quality-1)*quality+i+2], self.sphere[quality*quality+1]))
        self.faces.append(Face(color, self.sphere[(quality-1)*quality+1], self.sphere[quality*quality+1], self.sphere[quality*quality]))
        
class Cylinder:
    def __init__(self, color, x, y, z, r, h, quality,turn=0, twist=0):
        self.cylinder = []
        changeH = 360/quality
        posH = 0
        for i in range(quality):
            self.cylinder.append((x + r * math.cos(math.radians(posH)),
                                y + r * math.sin(math.radians(posH)),
                                z+h/2))
            posH += changeH
        posH = twist
        for i in range(quality):
            self.cylinder.append((x + r * math.cos(math.radians(posH)),
                                y + r * math.sin(math.radians(posH)),
                                z-h/2))
            posH += changeH
        
        self.faces = []
        top = []
        for i in range(quality):
            top.insert(0, self.cylinder[i])
        self.faces.append(Face(color, *top))
        for i in range(quality-1):
            self.faces.append(Face(color, self.cylinder[i], self.cylinder[i+1], self.cylinder[i+1+quality], self.cylinder[i+quality]))
        self.faces.append(Face(color, self.cylinder[quality-1], self.cylinder[0], self.cylinder[quality], self.cylinder[2*quality-1]))
        self.faces.append(Face(color, *self.cylinder[quality:]))
        
class Torus:
    def __init__(self, color, x, y, z, r1, r2, quality, yaw=0, pitch=0,roll=0):
        self.torus = []
        posH = 0
        posZ = 0
        dM = (r2+r1)/2
        rM = (r2-r1)/2
        
        changeH = 360/quality
        changeZ = 360/quality
        
        for i in range(quality):
            for j in range(quality):
                tempX = x + (dM + rM*math.cos(math.radians(posZ)))*math.cos(math.radians(posH))
                tempY = y + (dM + rM*math.cos(math.radians(posZ)))*math.sin(math.radians(posH))
                tempZ = z + rM*math.sin(math.radians(posZ))
                """
                if(yaw!=0):
                    tempR = math.sqrt((tempX-x)**2 + (tempY-y)**2)
                    tempAngle = math.degrees(math.atan2(tempY - y, tempX - x))
                    tempX = x + tempR * math.cos(math.radians(tempAngle + yaw))
                    tempY = y + tempR * math.sin(math.radians(tempAngle + yaw))
                if(pitch!=0):
                    tempR = math.sqrt((tempX-x)**2 + (tempZ-z)**2)
                    tempAngle = math.degrees(math.atan2(tempZ - z, tempX - x))
                    tempX = x + tempR * math.cos(math.radians(tempAngle + pitch))
                    tempZ = z + tempR * math.sin(math.radians(tempAngle + pitch))
                if(roll!=0):
                    tempR = math.sqrt((tempY-y)**2 + (tempZ-z)**2)
                    tempAngle = math.degrees(math.atan2(tempZ - z, tempY - y))
                    tempY = y + tempR * math.cos(math.radians(tempAngle + roll))
                    tempZ = z + tempR * math.sin(math.radians(tempAngle + roll))
                """
                tempRYaw = math.sqrt((tempX-x)**2 + (tempY-y)**2)
                tempRPitch = math.sqrt((tempX-x)**2 + (tempZ-z)**2)
                tempRRoll = math.sqrt((tempY-y)**2 + (tempZ-z)**2)
                
                tempAngleYaw = math.degrees(math.atan2(tempY - y, tempX - x))
                tempAnglePitch = math.degrees(math.atan2(tempZ - z, tempX - x))
                tempAngleRoll = math.degrees(math.atan2(tempZ - z, tempY - y))
                
                tempX = x + tempRYaw * math.cos(math.radians(tempAngleYaw + yaw)) + tempRPitch * math.cos(math.radians(tempAnglePitch + pitch))
                tempY = y + tempRYaw * math.sin(math.radians(tempAngleYaw + yaw)) + tempRRoll * math.cos(math.radians(tempAngleRoll + roll))
                tempZ = z + tempRPitch * math.sin(math.radians(tempAnglePitch + pitch)) + tempRRoll * math.sin(math.radians(tempAngleRoll + roll))
                #"""
                self.torus.append((tempX, tempY, tempZ))
                
                posZ += changeZ
            posZ = 0
            posH += changeH
        
        self.faces = []
        for i in range(quality-1):
            for j in range(quality-1):
                self.faces.append(Face(color, self.torus[i*quality+j], self.torus[i*quality+j+1], self.torus[(i+1)*quality+j+1], self.torus[(i+1)*quality+j]))
            self.faces.append(Face(color, self.torus[(i+1)*quality-1], self.torus[i*quality], self.torus[(i+1)*quality], self.torus[(i+2)*quality-1]))
        for i in range(quality-1):
            self.faces.append(Face(color, self.torus[(quality-1)*quality+i], self.torus[(quality-1)*quality+i+1], self.torus[i+1], self.torus[i]))
        self.faces.append(Face(color, self.torus[quality*quality-1], self.torus[(quality-1)*quality], self.torus[0], self.torus[quality-1]))

class LightSource:
    def __init__(self, color, x, y, z, r, quality):
        self.sphere = []
        posH = 0
        posZ = 90
        changeH = 360/quality
        changeZ = 180/(quality+1)
        self.sphere.append((x,y,z-r))
        posZ += changeZ
        for i in range(quality):
            for j in range(quality):
                self.sphere.append((x - r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    y - r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)),
                                    z - r * math.sin(math.radians(posZ))))
                posH += changeH
            posH=0
            posZ += changeZ
        self.sphere.append((x,y,z+r))
        
        self.faces = []
        for i in range(quality-1):
            self.faces.append(Face(color, self.sphere[0], self.sphere[i+2], self.sphere[i+1]))
        self.faces.append(Face(color, self.sphere[0], self.sphere[1], self.sphere[quality]))
        for i in range(quality-1):
            for j in range(quality-1):
                self.faces.append(Face(color, self.sphere[i*quality+j+1], self.sphere[i*quality+j+2], self.sphere[(i+1)*quality+j+2], self.sphere[(i+1)*quality+j+1]))
            self.faces.append(Face(color, self.sphere[(i+1)*quality], self.sphere[i*quality+1], self.sphere[(i+1)*quality+1], self.sphere[(i+2)*quality]))
        for i in range(quality-1):
            self.faces.append(Face(color, self.sphere[(quality-1)*quality+i+2], self.sphere[quality*quality+1], self.sphere[(quality-1)*quality+i+1]))
        self.faces.append(Face(color, self.sphere[(quality-1)*quality+1], self.sphere[quality*quality+1], self.sphere[quality*quality]))
        
global size;
size = [900,550]
RED = (255,0,0)
GREEN = (100,255,100)
BLUE = (0,0,255)
PURPLE = (200,0,200)
ORANGE = (255,100,0)
BROWN = (100,50,30)
WHITE = (255,255,255)
speed = 40   #float(input("How fast do you want to go?(FPS)"))
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Perspective")
x = False

clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
screen.fill([0,0,0])
posH = .001
posZ = .001

realX = .01
realY = .01
realZ = 1.5
origin = [0,0,0]
light = [0,0,5]
r = 10
movement = .25
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
#shapes.append(SquarePyramid(-100,-100,-100,90,90,50))
"""
shapes.append(Sphere((200,200,200), 36,0,0,.0015,10))
shapes.append(Sphere((200,100,30), 67,0,0,.0037,10))
shapes.append(Sphere(GREEN, 93,0,0,.004,10))
shapes.append(Sphere((150,150,150), 93,.238,0,.001,10))
shapes.append(Sphere((200,0,0), 141.6,0,0,.0021,10))
shapes.append(Sphere((207,157,52), 483.5,0,0,.0444,10))
shapes.append(Sphere((255,200,100), 888.8,0,0,.0375,10))
shapes.append(Torus((220,220,220), 888.8,0,0,.0571, .0731,20))
shapes.append(Torus((170,170,170), 888.8,0,0,.0759, .085,20))
shapes.append(Sphere((76,220,252),1783.7,0,0,.016,10))
shapes.append(Sphere((50,123,250),2797.8,0,0,.015,10))
"""
#shapes.append(Torus(RED, 8,0,2,2,2.7,20, 0, 15, 15))
#shapes.append(Torus(GREEN, 8,0,2,2.7,3.4,20, 0, 15, 15))
#shapes.append(Torus(BLUE, 8,0,2,3.4,4.1,20, 0, 15, 15))
#shapes.append(LightSource((255,255,0), light[0], light[1], light[2], .5,10))
#shapes.append(Cube(GREEN, 5,3,-3,2,2,2))
#shapes.append(Sphere(PURPLE, 9,0,2,1.3,18))
"""
shapes.append(Sphere(BROWN, 8,0,0,1.3,15))
shapes.append(Sphere(BROWN, 10,0,0,1.3,15))
shapes.append(Cylinder(BROWN, 9,0,2.5, 1.4, 5, 50, 90, 0))
shapes.append(Sphere(BROWN, 9,0,5,1.4,18))
#"""
#shapes.append(Sphere(4,4,9,2,6))
#shapes.append(Sphere(4,4,12,1,4))
"""
shapes.append(Cube(GREEN, -1,-1,-1,2,2,2))
shapes.append(Cube(GREEN, -3,-1,-1,2,2,2))
shapes.append(Cube(GREEN, 1,-1,-1,2,2,2))
shapes.append(Cube(GREEN, 3,-1,-1,2,2,2))
shapes.append(Cube(GREEN, 3,-1,1,2,2,2))
shapes.append(Cube(GREEN, 3,-1,3,2,2,2))
shapes.append(Cube(GREEN, 3,-1,-3,2,2,2))
shapes.append(Cube(GREEN, 3,-1,-5,2,2,2))
shapes.append(Cube(GREEN, -3,-1,1,2,2,2))
shapes.append(Cube(GREEN, -3,-1,3,2,2,2))
shapes.append(Cube(GREEN, -3,-1,-3,2,2,2))
shapes.append(Cube(GREEN, -3,-1,-5,2,2,2))
#shapes.append(Cube(7,-1,1,2,2,2))
#shapes.append(Cube(7,-1,-3,2,2,2))
#shapes.append(Cube(7,-1,-5,2,2,2))
#"""
#shapes.append(Cylinder(RED, 8,0,-5, 1.4, 4, 50, 90, 0))
#shapes.append(SquarePyramid(PURPLE, 4,0,-3, 2,2,2))
#"""

rows = 16
cols = 8
width = 3
height = 1

maze = [[[False,1,1,1,1] for x in range(cols)] for x in range(rows)]
def inBounds(a,b):
    return a>=0 and b>=0 and a<rows and b<cols


def goTo(a, b):
    possible = []

    if(inBounds(a-1, b) and not maze[a-1][b][0]):
        possible.append(1)
    if(inBounds(a, b+1) and not maze[a][b+1][0]):
        possible.append(2)
    if(inBounds(a+1, b) and not maze[a+1][b][0]):
        possible.append(3)
    if(inBounds(a, b-1) and not maze[a][b-1][0]):
        possible.append(4)
    
    maze[a][b][0] = True
    if(possible.__len__() == 0):
        return 0
    #return possible[random.randrange(0,possible.__len__())]
    #return choice(possible)
    #"""
    evens = list(filter(lambda x : x%2==0, possible))
    odds = list(filter(lambda x : x%2==1, possible))
    
    if(evens.__len__()==0):
        return choice(odds)
    if(odds.__len__()==0):
        return choice(evens)
    if(.5*abs(peek[0]-X)>abs(peek[1]-Y)):
        if(random.randrange(0,10)<9):
            return choice(evens)
        else:
            return choice(odds)
    elif(abs(peek[0]-X)>abs(peek[1]-Y)):
        return choice(possible)
    elif(abs(peek[0]-X)<.5*abs(peek[1]-Y)):
        if(random.randrange(0,10)<9):
            return choice(odds)
        else:
            return choice(evens)
    else:
        return choice(possible)
    #"""
X = rows//2
Y = cols//2
stack = []
stack.append([0,0])

while(not stack.__len__() == 0):
    peek = []
    peek.append(stack[stack.__len__()-1][0])
    peek.append(stack[stack.__len__()-1][1])
    direction = goTo(peek[0], peek[1])
    #print("Before = "+str(peek[0]) +" "+ str(peek[1]))
    maze[peek[0]][peek[1]][0] = True
    if(direction==0):
        stack.pop()
    else:
        maze[peek[0]][peek[1]][direction] = 0
        if(direction==1):
            peek[0] -= 1
            maze[peek[0]][peek[1]][3] = 0
        elif(direction==2):
            peek[1] += 1
            maze[peek[0]][peek[1]][4] = 0
        elif(direction==3):
            peek[0] += 1
            maze[peek[0]][peek[1]][1] = 0
        elif(direction==4):
            peek[1] -= 1
            maze[peek[0]][peek[1]][2] = 0
        stack.append([peek[0], peek[1]])
    
maze[0][0][4] = 0
maze[maze.__len__()-1][maze[0].__len__()-1][2] = 0

for i in range(rows+1):
    for j in range(cols+1):
        for h in range(height):
            shapes.append(Cube(GREEN, j*width,i*width,h,1,1,1))

for i in range(rows):
        for j in range(cols):
            if(maze[i][j][1]==1):
                for h in range(height):
                    for w in range(1,width):
                        shapes.append(Cube(GREEN, j*width+w,i*width,h,1,1,1))

            if(maze[i][j][4]==1):
                for h in range(height):
                    for w in range(1,width):
                        shapes.append(Cube(GREEN, j*width,i*width+w,h,1,1,1))

            if(i==rows-1 or j ==cols-1):
                if(maze[i][j][2]==1):
                    for h in range(height):
                        for w in range(1,width):
                            shapes.append(Cube(GREEN, j*width+width,i*width+w,h,1,1,1))
                            
                if(maze[i][j][3]==1):
                    for h in range(height):
                        for w in range(1,width):
                            shapes.append(Cube(GREEN, j*width+w,i*width+width,h,1,1,1))
            
    




while x == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = True
            #uprint("quit")
    
    keyboard = pygame.key.get_pressed()
    
    if keyboard[pygame.K_LEFT] == 1:
        posH-=5
        if posH<0:
            posH=359
    if keyboard[pygame.K_RIGHT] == 1:
        posH+=5
        if posH>=360:
            posH=0
    if keyboard[pygame.K_DOWN] == 1:
        posZ-=5
        if(posZ<-89):
            posZ += 5
    if keyboard[pygame.K_UP] == 1:
        posZ+=5
        if(posZ>89):
            posZ -= 5
    if keyboard[pygame.K_w] == 1:
        realX += movement * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += movement * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realZ += movement * math.sin(math.radians(posZ))
    if keyboard[pygame.K_s] == 1:
        realX += -movement * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
        realY += -movement * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
        realZ += -movement * math.sin(math.radians(posZ))
    if keyboard[pygame.K_a] == 1:
        realX += movement * math.sin(math.radians(posH))# * abs(math.sin(math.radians(posZ)))
        realY += -movement * math.cos(math.radians(posH))# * abs(math.sin(math.radians(posZ)))
        #realX += math.sqrt((movement * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (movement * math.sin(math.radians(posZ)))**2)
        #realY += -math.sqrt((movement * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (movement * math.sin(math.radians(posZ)))**2)
    if keyboard[pygame.K_d] == 1:
        realX += -movement * math.sin(math.radians(posH))# * abs(math.sin(math.radians(posZ)))
        realY += movement * math.cos(math.radians(posH)) #* abs(math.sin(math.radians(posZ)))
    if keyboard[pygame.K_q] == 1:
        realX += movement * math.cos(math.radians(posH)) * math.sin(math.radians(posZ))
        realY += movement * math.sin(math.radians(posH)) * math.sin(math.radians(posZ))
        realZ += -math.sqrt((movement * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (movement * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)))**2)
    if keyboard[pygame.K_2] == 1:
        realX += -movement * math.cos(math.radians(posH)) * math.sin(math.radians(posZ))
        realY += -movement * math.sin(math.radians(posH)) * math.sin(math.radians(posZ))
        realZ += math.sqrt((movement * math.cos(math.radians(posH)) * math.cos(math.radians(posZ)))**2 + (movement * math.sin(math.radians(posH)) * math.cos(math.radians(posZ)))**2)
    if keyboard[pygame.K_t] == 1:
        realX, realY, realZ = origin
    origin[0] = realX + r * math.cos(math.radians(posH)) * math.cos(math.radians(posZ))
    origin[1] = realY + r * math.sin(math.radians(posH)) * math.cos(math.radians(posZ))
    origin[2] = realZ + r * math.sin(math.radians(posZ))
    """
    light[0] = realX
    light[1] = realY
    light[2] = realZ
    """
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
    """
    centerDists = []
    for face in faces:
        centerDists.append(math.sqrt((realX - face.center[0])**2 + (realY - face.center[1])**2 + (realZ - face.center[2])**2))
    
    for i in range(faces.__len__()-1):
        for j in range(faces.__len__()-1-i):
            if(centerDists[j] < centerDists[j+1]):
                temp = faces[j]
                faces[j] = faces[j+1]
                faces[j+1] = temp
                temp = centerDists[j]
                centerDists[j] = centerDists[j+1]
                centerDists[j+1] = temp
    #"""
    faces = sorted(faces, key = lambda face:face.getDist(realX, realY, realZ), reverse = True)
    screen.fill([0,0,0])
    calculatedCorners = {}
    for face in faces:
        
        angleD = []
        angleR = []
        for corner in face.corners:
            if(corner not in calculatedCorners):
                angleD.append( math.degrees( math.acos( ( (origin[0] - realX)*(corner[0] - realX) + (origin[1] - realY)*(corner[1] - realY) + (origin[2] - realZ)*(corner[2] - realZ) ) 
                                                        / ( math.sqrt( ( origin[0] - realX)**2 + ( origin[1] - realY)**2 + ( origin[2] - realZ)**2 ) *  math.sqrt( ( corner[0] - realX)**2 + ( corner[1] - realY)**2 + ( corner[2] - realZ)**2 ) ) ) ) )
                
                t = - ( (origin[0] - realX)*(realX - corner[0]) + (origin[1] - realY)*(realY - corner[1]) + (origin[2] - realZ)*(realZ - corner[2]) ) / ( (origin[0] - realX)**2 + (origin[1] - realY)**2 + (origin[2] - realZ)**2 )
                vertex = [realX + (origin[0] - realX)*t, realY + (origin[1] - realY)*t, realZ + (origin[2] - realZ)*t]
                perpendicular = [vertex[0] - (origin[1] - realY), vertex[1] + (origin[0] - realX), vertex[2]]
                #print( math.sqrt( ( perpendicular[0] - vertex[0])**2 + ( perpendicular[1] - vertex[1])**2 + ( perpendicular[2] - vertex[2])**2 ) *  math.sqrt( ( corner[0] - vertex[0])**2 + ( corner[1] - vertex[1])**2 + ( corner[2] - vertex[2])**2 ) )
                tempR = ( (perpendicular[0] - vertex[0])*(corner[0] - vertex[0]) + (perpendicular[1] - vertex[1])*(corner[1] - vertex[1]) + (perpendicular[2] - vertex[2])*(corner[2] - vertex[2]) ) / ( math.sqrt( ( perpendicular[0] - vertex[0])**2 + ( perpendicular[1] - vertex[1])**2 + ( perpendicular[2] - vertex[2])**2 ) *  math.sqrt( ( corner[0] - vertex[0])**2 + ( corner[1] - vertex[1])**2 + ( corner[2] - vertex[2])**2 ) )
                if(tempR<-1):
                    tempR = -1
                if(tempR>1):
                    tempR = 1
                #print(tempR)
                R = math.acos( tempR )
                if(corner[2]<perpendicular[2]):
                    angleR.append(2*math.pi - R)
                else:
                    angleR.append(R)
                    
                calculatedCorners[corner] = (angleD[len(angleD)-1], angleR[len(angleR)-1])
            else:
                D, R = calculatedCorners[corner]
                angleD.append(D)
                angleR.append(R)
            
        #print(angleD)
        points = []
        behind = False
        for i in range(face.corners.__len__()):
            if(angleD[i]>150):
                behind = True
            points.append((450+angleD[i]*15*math.cos(angleR[i]), 275-angleD[i]*15*math.sin(angleR[i])))
            
        shading = math.degrees( math.acos( ( (light[0] - face.center[0])*(face.normal[0] - face.center[0]) + (light[1] - face.center[1])*(face.normal[1] - face.center[1]) + (light[2] - face.center[2])*(face.normal[2] - face.center[2]) ) 
                                                / ( math.sqrt( ( light[0] - face.center[0])**2 + ( light[1] - face.center[1])**2 + ( light[2] - face.center[2])**2 ) *  math.sqrt( ( face.normal[0] - face.center[0])**2 + ( face.normal[1] - face.center[1])**2 + ( face.normal[2] - face.center[2])**2 ) ) ) ) / 180
        #shading = 1
        if(not behind):
            pygame.draw.polygon(screen, face * shading, points, 0)
            #pygame.draw.polygon(screen, (0,0,0), points, 1)
            #pygame.draw.aalines(screen, face * shading,True, points, 1)
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
        #pygame.display.flip()
        #pygame.time.delay(20)
    #pygame.draw.circle(screen, (0,0,0),(450,275),3,0)
    
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

    pygame.display.flip()
    clock.tick(speed)
pygame.quit()