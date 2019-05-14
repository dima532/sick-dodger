import sys,pygame
import math
import time
from mouseshot import mouseshoot as ms
import random as r
pygame.init()
(width, height) = (726, 726)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sick dodger")
#textures
walkRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/7.png'))]

walkLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/7.png'))]

walkfaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

walktous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/7.png'))]

chRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/7.png'))]

chLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/7.png'))]

chfaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

chtous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/7.png'))]

fireRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/7.png'))]

fireLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/7.png'))]

firefaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

firetous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/4.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/5.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/6.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/7.png'))]

bull=[pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/1.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/2.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/3.png')),
pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/4.png'))]

hp=[pygame.transform.scale2x(pygame.image.load('sphere drone/battery/3.png')),
    pygame.transform.scale2x(pygame.image.load('sphere drone/battery/2.png')),
    pygame.transform.scale2x(pygame.image.load('sphere drone/battery/1.png')),
    pygame.transform.scale2x(pygame.image.load('sphere drone/battery/0.png'))]

bg= pygame.image.load('sphere drone/fone.png')

kres0=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/4.png')),]

kres1=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/4.png')),]

kres2=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/4.png')),]

kres3=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/4.png')),]

kres4=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/4.png')),]

tor0l=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 0/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 0/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 0/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 0/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 0/5.png'))]

tor1l=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 1/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 1/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 1/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 1/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 1/5.png'))]

tor2l=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 2/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 2/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 2/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 2/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 2/5.png'))]

tor3l=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 3/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 3/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 3/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 3/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sl/charge 3/5.png'))]

tor0r=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 0/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 0/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 0/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 0/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 0/5.png'))]

tor1r=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 1/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 1/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 1/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 1/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 1/5.png'))]

tor2r=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 2/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 2/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 2/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 2/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 2/5.png'))]

tor3r=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 3/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 3/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 3/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 3/4.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/torture/sr/charge 3/5.png'))]

portal=[pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/7.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/8.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/spawn portal/9.png')),]

yadro=pygame.transform.scale2x(pygame.image.load('sphere drone/1 s bullet.png'))
bj=-1
pygame.font.init()
scorefont= pygame.font.SysFont('Comic Sans MS', 72)
con=2;
#textures end
clock = pygame.time.Clock() #задание инициализации времени простым текстом

def spawnkrbul(j):
    listoz.list.append(yedro(listos.list[j].x, listos.list[j].y, 1, 1))
    listoz.list.append(yedro(listos.list[j].x, listos.list[j].y, 2, 1))
    listoz.list.append(yedro(listos.list[j].x, listos.list[j].y, 3, 1))
    listoz.list.append(yedro(listos.list[j].x, listos.list[j].y, 4, 1))
    listoz.j+=4
    listos.list[j].chargecount=0

class health():#класс для батарейки
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.hp=3

    def draw(self, screen):#рисовка
        screen.blit(hp[3-self.hp],(self.x,self.y))

class enemy():#родительский класс противников
    def __init__(self, x, y, a):
        self.x=x
        self.y=y
        self.speedy = 2
        self.speedx = 2
        self.firecount = 0
        self.walkcount = 0
        self.walkdir=a
        
class enembulmanager():
    def __init__(self):
        self.list=[]
        self.j=-1
    
    def bulwalk(self, rect):
        j=self.j
        while j>=0:
            if self.list[j].klass=="yadro":
                if self.list[j].typ==1:
                    self.list[j].movekr()
                if self.list[j].typ==2:
                    self.list[j].movegor()
                self.list[j].rect=pygame.Rect(self.list[j].x,self.list[j].y,32,32)
            
            if self.list[j].x<=0 or self.list[j].x>=width:
                self.list[j].isexist= False
            elif self.list[j].y<=0 or self.list[j].y>=height:
                self.list[j].isexist=False
            else:
                self.list[j].isexist=True
            if self.list[j].rect.colliderect(rect):
                hitself()
                j=0
                break
            if not self.list[j].isexist:
                self.list.pop(j)
                self.j-=1
            j-=1

    def drawall(self, screen):
        j=self.j
        while j>=0:
            self.list[j].draw(screen)
            j-=1
            
        
class enemymanager():
    def __init__(self):
        self.list=[]
        self.bullist=[]
        self.j=-1


    def walkall(self,bj):
        j=self.j
        score=0
        while j>=0:
            if self.list[j].clas == "krest":
                self.list[j].x+=self.list[j].speedx
                self.list[j].y+=self.list[j].speedy
                if (self.list[j].y>=height-self.list[j].dc or self.list[j].y<=0-self.list[j].uc):
                    self.list[j].speedy=-self.list[j].speedy
                if (self.list[j].x>=width-self.list[j].rc or self.list[j].x<=0-self.list[j].lec):
                    self.list[j].speedx=-self.list[j].speedx
            if self.list[j].clas == "torture":
                self.list[j].y+=self.list[j].speed
                if self.list[j].y>=height-self.list[j].dc or self.list[j].y<=0-self.list[j].uc:
                    self.list[j].speed=-speed
            self.list[j].rect=pygame.Rect(self.list[j].x+self.list[j].lec, self.list[j].y+self.list[j].uc, self.list[j].rc-self.list[j].lec, self.list[j].dc-self.list[j].uc)
            bj2=bj
            
            self.list[j].draw(screen)
            if self.list[j].chargecount>70:
                spawnkrbul(j)
            while bj2>=0:
                if self.list[j].rect.colliderect(self.bullist[bj2].rect):
                    self.list.pop(j)
                    self.j-=1
                    self.bullist.pop(bj2)
                    bj-=1
                    score+=1
                bj2-=1
            j-=1
        return [bj, score]
            
    def enemblit(self, screen):#для прорисовки ВСЕХ врагов, не рабочий вид
        ej=0
        while ej<j:
             self.list[j].draw(screen)
             ej+=1

class krest(enemy):#дочерний класс к "враг": "крестовой"
    def __init__(self, x, y, a):
        self.x=x
        self.y=y
        if a==1:
            self.speedy = 2
            self.speedx = 2
        if a==2:
            self.speedy = -2
            self.speedx = 2
        if a==3:
            self.speedy = 2
            self.speedx = -2
        if a==4:
            self.speedy = -2
            self.speedx = -2
        self.health = 1
        self.firecount = 0
        self.walkcount = 0
        self.chargecount = 0
        self.clas="krest"
        self.lec=5*con;
        self.dc=31*con;
        self.rc=30*con;
        self.uc=0*con;
        self.rect= kres0[0].get_rect()
        
    def draw(self, screen):
        if self.walkcount+1 >= 20:
            self.walkcount = 0
        if self.chargecount<=70/5:
            screen.blit(kres0[self.walkcount//5],(self.x,self.y))
        elif self.chargecount>=70/5 and self.chargecount<=70/5*2:
            screen.blit(kres1[self.walkcount//5],(self.x,self.y))
        elif self.chargecount>=70/5*2 and self.chargecount<=70/5*3:
            screen.blit(kres2[self.walkcount//5],(self.x,self.y))
        elif self.chargecount>=70/5*3 and self.chargecount<=70/5*4:
            screen.blit(kres3[self.walkcount//5],(self.x,self.y))
        elif self.chargecount>=70/5*4:
            screen.blit(kres4[self.walkcount//5],(self.x,self.y))
        self.walkcount+=1
        self.chargecount+=1

class torture(enemy):
    def __init__(self,x,y,a):
        self.x=x
        self.y=y
        if a==1:
            self.speed = 2
        if a==2:
            self.speed = -2
        self.health = 1
        self.firecount = 0
        self.walkcount = 0
        self.chargecount = 0
        self.clas="torture"
        self.lec=5*con;
        self.dc=31*con;
        self.rc=30*con;
        self.uc=0*con;
        self.rect= kres0[0].get_rect()

    def draw(self,screen):
        self.wal

class bullet():#класс для пули
    def __init__(self, x, y, c):
        self.x=x
        self.y=y
        self.speed = 10
        self.walkcount=0
        self.isexist= True
        bulx=pygame.mouse.get_pos()[0]
        buly=pygame.mouse.get_pos()[1]
        self.kaef=self.speed/(((bulx-x)*(bulx-x)+(buly-y)*(buly-y))**0.5)
        self.speedx=(bulx-x)*self.kaef
        self.speedy=(buly-y)*self.kaef
        self.lec=2*con
        self.dc=19*con
        self.rc=19*con
        self.uc=2*con
        self.rect= bull[0].get_rect()
        

    def draw(self, screen):
        if self.walkcount + 1 >= 20:
            self.walkcount=0
        screen.blit(bull[self.walkcount//5],(self.x,self.y) )
        self.walkcount+=1


class yedro():
    def __init__(self,x,y,direct,typ):
        self.x=x
        self.y=y
        self.rect= yadro.get_rect()
        self.speed=5
        self.direct=direct
        self.typ=typ
        self.isexist= True
        self.klass="yadro"

    def draw(self,screen):
        screen.blit(yadro,(self.x,self.y))

    def movekr(self):
        if self.direct==1:
            self.x+=self.speed
            self.y+=self.speed
        elif self.direct==2:
            self.x-=self.speed
            self.y+=self.speed
        elif self.direct==3:
            self.x+=self.speed
            self.y-=self.speed
        elif self.direct==4:
            self.x-=self.speed
            self.y-=self.speed

    def movegor(self):
        if self.direct==1:
            self.x-=self.speed
        elif self.direct==2:
            self.x+=self.speed
        
        

class player():#класс игрока
    def __init__(self, x, y, a, b):
        self.x=x
        self.y=y
        self.a = a
        self.b = b
        self.speed = 4
        self.wleft = True
        self.wright = False
        self.wtus = False
        self.wfaraw = False
        self.walkcount=0
        self.chargecount=0
        self.rect=pygame.Rect(x,y,32,32)


    def draw(self, screen):
        if self.walkcount + 1 >= 35:
            self.walkcount=0
        self.walkcount+=1
        if self.chargecount<=30:
            if self.wtus:
                screen.blit(walktous[self.walkcount//5],(self.x,self.y) )
            elif self.wfaraw:
                screen.blit(walkfaraway[self.walkcount//5],(self.x,self.y) )
            elif self.wleft:
                screen.blit(walkLeft[self.walkcount//5],(self.x,self.y) )
            elif self.wright:
                screen.blit(walkRight[self.walkcount//5],(self.x,self.y) )
        elif self.chargecount<80 and self.chargecount>30:
            if self.wtus:
                screen.blit(chtous[self.walkcount//5],(self.x,self.y) )
            elif self.wfaraw:
                screen.blit(chfaraway[self.walkcount//5],(self.x,self.y) )
            elif self.wleft:
                screen.blit(chLeft[self.walkcount//5],(self.x,self.y) )
            elif self.wright:
                screen.blit(chRight[self.walkcount//5],(self.x,self.y) )
        else:
            if self.wtus:
                screen.blit(firetous[self.walkcount//5],(self.x,self.y) )
            elif self.wfaraw:
                screen.blit(firefaraway[self.walkcount//5],(self.x,self.y) )
            elif self.wleft:
                screen.blit(fireLeft[self.walkcount//5],(self.x,self.y) )
            elif self.wright:
               screen.blit(fireRight[self.walkcount//5],(self.x,self.y) )


        if self.chargecount>=200:
            self.chargecount+=0
        else:
            self.chargecount+=1

class heal():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.rect=228

def bulcheck(i,bj):#уже рабочая штука для удаления пули(работать перестала)
    bulpop=0
    if listos.bullist[i].x>=width or listos.bullist[i].x<=0:
        listos.bullist[i].isexist=False
    if listos.bullist[i].y>=height or listos.bullist[i].y<=0:
        listos.bullist[i].isexist=False
    if not (listos.bullist[i].isexist):
        listos.bullist.pop(i)
        bj-=1
    return [bj,i]

    

def redrawGameWindow():#перерисовка окна
    screen.blit(screen,(0,0))
    myhp.draw(screen)
    j=bj
    while j>=0:
        if listos.bullist[j].isexist:
            listos.bullist[j].draw(screen)
        j-=1
    man.draw(screen)
    listos.enemblit(screen)
    pygame.display.update()
    screen.blit(scores,(scorex,0))
    listoz.drawall(screen)
running = True

def hitself():#РАБОТАЕТ!!! УРЯ!!!
    myhp.hp-=1
    listoz.list=[]
    listoz.j=-1
    j2=listos.j
    if j2>=0:
        listos.list[j2].chargecount-=70
        j2-=1


def healself(j):
    if myhp.hp<3:
        myhp.hp+=1
    
    




#mainloop
scorex=width
scorei=0
scores=scorefont.render(str(scorei), False, (0,0,0))
i=-1
part=1
man = player(width/2,height/2,32,32)
healist=[]
torture = []
spiked=[]
kr=[]
j=-1
b=0
newx=0
newy=0
telek=[]
timerforport=int(0)
timerportsprite=5
someshit=False
listos = enemymanager()
listoz = enembulmanager()
encount=0
timerforenemy=0
myhp=health(5,2)
something=False
playing=True
while running:
    if playing:
        redrawGameWindow()
        if i>3:
            i=0
        bij=[]
        clock.tick(180)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        #key input
        if keys[pygame.K_d] and keys[pygame.K_a]:
            man.wleft=False
            man.wright=True
            man.wfaraw=False
            man.wtus=False

        elif keys[pygame.K_a] and man.x>man.speed:
            man.x -= man.speed
            man.wleft = True
            man.wright =False
            man.wfaraw=False
            man.wtus=False

        elif keys[pygame.K_d] and man.x < width-man.a-man.speed:
            man.x += man.speed
            man.wleft=False
            man.wright=True
            man.wfaraw=False
            man.wtus=False

        if keys[pygame.K_s]and keys[pygame.K_w]:
            man.wleft=False
            man.wright = False
            man.wfaraw=False
            man.wtus=True

        elif keys[pygame.K_w] and man.y>man.speed:
            man.y -= man.speed
            man.wleft=False
            man.wright = False
            man.wfaraw=True
            man.wtus=False

        elif keys[pygame.K_s]and man.y < height-man.a-man.a-man.speed:
            man.y += man.speed
            man.wleft=False
            man.wright = False
            man.wfaraw=False
            man.wtus=True
        man.chargecount+=1
        #key input end
        if man.chargecount>80 and pygame.mouse.get_pressed()[0]:#input for shoot
                listos.bullist.append(bullet(man.x+12,man.y+12,1))
                man.chargecount=0
                bj+=1
        j=bj
        if keys[pygame.K_KP9]:#input to hurt myself
            if not (something):
                hitself()
                something=True
        else:
            something = False
        while j>=0:
            listos.bullist[j].x+=listos.bullist[j].speedx
            listos.bullist[j].y+=listos.bullist[j].speedy
            listos.bullist[j].rect=pygame.Rect(listos.bullist[j].x+listos.bullist[j].lec, listos.bullist[j].y+listos.bullist[j].uc, listos.bullist[j].rc-listos.bullist[j].lec, listos.bullist[j].dc-listos.bullist[j].uc)
            bij=bulcheck(j,bj)
            bj=bij[0]
            j=bij[1]
            j-=1
        timerforenemy+=1
        if b<30 and scorei<30:
            if timerforenemy>=90:#enemy spawn timer
                if not someshit:
                    newt=r.randint(1,1)
                    newx=r.randint(0,width-60)
                    newy=r.randint(0,height-74)
                    someshit=True
                    
                if timerforport>=4*timerportsprite:
                    if newt==1:
                        screen.blit(kres0[0],(newx,newy))
                    elif newt==2:
                        screen.blit(tor0l[0],(newx,newy))
                if timerforport>8*timerportsprite:
                    listos.j+=1
                    timerforport=0
                    if newt==1:
                        listos.list.append(krest(newx,newy,1))#крест + 1 в список
                    if newt==2:
                        listos.list.append(torture(newx,newy,1))
                    b+=1
                    someshit=False
                    timerforenemy=0#enemy spawn timer = 0
                screen.blit(portal[int(timerforport/timerportsprite)],(newx+10,newy+10))
                timerforport+=1
        elif b>=30 and scorei>=30:
            if telek==[]:
                telek=[0]
        pygame.display.flip()
        screen.blit(bg,(0,0))
        bij=listos.walkall(bj)

        scorex=width
        scorei2=int(scorei)
        while True:
            scorex-=43
            if scorei2/10<1:
                scorei2=0
            else:
                scorei2/=10
            if scorei2==0:
                break
        scores=scorefont.render(str(scorei), False, (0,0,0))
        if scorei>=30:
            scores=scorefont.render(str(scorei), False, (255,0,0))
        bj=bij[0]
        scorei+=bij[1]
        man.rect=pygame.Rect(man.x,man.y,32,32)
        listoz.bulwalk(man.rect)
        if myhp.hp<=0:
            running=False
