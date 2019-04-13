import sys,pygame
import math
import time
from mouseshot import mouseshoot as ms
import random as r
pygame.init()
(width, height) = (484, 484)
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

bg= pygame.transform.scale2x(pygame.image.load('sphere drone/fone.png'))

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
#textures end
clock = pygame.time.Clock() #задание инициализации времени простым текстом

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

class enemymanager():
    def __init__(self):
        self.list=[]

    def gotovnost(self,torture, spiked, kr):
        self.list = torture + spiked + kr


    def walkall(self,j1,j2,j3):
        j=j1+j2+j3-1
        while j>=0:
            if self.list[j].clas == "krest":
                if kr[j].walkdir == 1:
                    kr[j].x+=kr[j].speedx
                    kr[j].y+=kr[j].speedy
                b1=False
                b2=False
                if (kr[j].y>=height-74 or kr[j].y<=0):
                    kr[j].speedy=-kr[j].speedy
                if (kr[j].x>=width-50 or kr[j].x<=0):
                    kr[j].speedx=-kr[j].speedx
            j-=1
    
class krest(enemy):#дочерний класс к врагу: "крестовой"
    def __init__(self, x, y, a):
        self.x=x
        self.y=y
        self.speedy = 2
        self.speedx = 2
        self.firecount = 0
        self.walkcount = 0
        self.walkdir=a
        self.clas="krest"

    def draw(self, screen):
        if self.walkcount+1 >= 20:
            self.walkcount = 0
        screen.blit(kres0[self.walkcount//5],(self.x,self.y))
        self.walkcount+=1

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

    def draw(self, screen):
        if self.walkcount + 1 >= 20:
            self.walkcount=0
        screen.blit(bull[self.walkcount//5],(self.x-21,self.y-21) )
        self.walkcount+=1

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


    def draw(self, screen):
        if self.walkcount + 1 >= 35:
            self.walkcount=0
        self.walkcount+=1
        if self.chargecount<=30:
            if self.wtus:
                screen.blit(walktous[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wfaraw:
                screen.blit(walkfaraway[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wleft:
                screen.blit(walkLeft[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wright:
                screen.blit(walkRight[self.walkcount//5],(self.x-12,self.y-12) )
        elif self.chargecount<80 and self.chargecount>30:
            if self.wtus:
                screen.blit(chtous[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wfaraw:
                screen.blit(chfaraway[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wleft:
                screen.blit(chLeft[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wright:
                screen.blit(chRight[self.walkcount//5],(self.x-12,self.y-12) )
        else:
            if self.wtus:
                screen.blit(firetous[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wfaraw:
                screen.blit(firefaraway[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wleft:
                screen.blit(fireLeft[self.walkcount//5],(self.x-12,self.y-12) )
            elif self.wright:
               screen.blit(fireRight[self.walkcount//5],(self.x-12,self.y-12) )


        if self.chargecount>=200:
            self.chargecount+=0
        else:
            self.chargecount+=1

def bulcheck(i):#уже рабочая штука для удаления пули
    if bul[i].x>=width or bul[i].x<=0:
        bul[i].isexist=False
    if bul[i].y>=height or bul[i].y<=0:
        bul[i].isexist=False
    if not (bul[i].isexist):
        list.pop([i])


def enemblit(screen):#для прорисовки ВСЕХ врагов, не конечый вид
    j=0
    while j<krcount:
         kr[j].draw(screen)
         j+=1

def redrawGameWindow():#перерисовка окна
    screen.blit(screen,(0,0))
    myhp.draw(screen)
    enemblit(screen)
    man.draw(screen)
    j=bj
    while j>=0:
        if bul[j].isexist:
            bul[j].draw(screen)
        j-=1
    pygame.display.update()
running = True

def hitself():#для проверки
    myhp.hp-=1

#mainloop
i=-1
part=1
man = player(width/2,height/2,32,32)
bul = []
torture = []
spiked=[]
kr=[]
j=-1
bj=-1
listos = enemymanager()
krcount=0
spicont=0
torturec=0
timerforenemy=0
myhp=health(5,2)
something=False
while running:
    if i>3:
        i=0
    clock.tick(60)
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
    b=not(keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a])
    #key input end
    if man.chargecount>=0 and pygame.mouse.get_pressed()[0]:#input for shoot
            bul.append(bullet(man.x,man.y,1))
            man.chargecount=0
            bj+=1
    j=bj
    if keys[pygame.K_KP9]:#input to hurt myself
        if not (something):
            hitself()
            something=True
    
    else:
        something = False
    if keys[pygame.K_q]:
        bul
    while j>=0:
        bul[j].x+=bul[j].speedx
        bul[j].y+=bul[j].speedy
        bulcheck(j)
        j-=1
    timerforenemy+=1
    if timerforenemy>=180:#enemy spawn timer
            timerforenemy=0#enemy spawn timer = 0
            krcount+=1#колличество врагов + 1
            kr.append(krest(r.randint(0,width-50),r.randint(0,height-74),1))#враг + 1 в список
    pygame.display.flip()
    screen.blit(bg,(0,0))
    redrawGameWindow()
    listos.gotovnost(torture, spiked, kr)
    listos.walkall(krcount,spicont,torturec)
    if myhp.hp<=0:
        running=False
