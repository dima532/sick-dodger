import sys,pygame
import time
import random as r
pygame.init()
(width, height) = (935, 438)
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

bg= pygame.image.load('sphere defence drone.png')

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

kres5=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/1.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/2.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/3.png')),
       pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/4.png')),]
#textures end
clock = pygame.time.Clock() #не знаю что

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
        
class krest(enemy):#дочерний класс к врагу: "крестовой"
    def draw(self, screen):
        if self.walkcount+1 >= 20:
            self.walkcount = 0
        screen.blit(kres0[self.walkcount//5],(self.x,self.y))
        self.walkcount+=1
            
class bullet():#класс для пули
    def __init__(self, x, y, c):
        self.x=x
        self.y=y
        self.speed = 5
        self.walkcount=0
        self.isexist= False
        self.direct=1
        self.direction=c
        
    def draw(self, screen):
        if self.walkcount + 1 >= 20:
            self.walkcount=0
        screen.blit(bull[self.walkcount//5],(self.x,self.y) )
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
        self.firi=False
        self.file=False
        self.fitu=False
        self.fifa=False
        self.walkcount=0
        self.chargecount=0


    def draw(self, screen):
        if self.walkcount + 1 >= 35:
            self.walkcount=0
            
        if self.wtus:
            self.walkcount+=1
            screen.blit(walktous[self.walkcount//5],(self.x,self.y) )
        elif self.wfaraw:
            self.walkcount+=1
            screen.blit(walkfaraway[self.walkcount//5],(self.x,self.y) )
        elif self.wleft:
            screen.blit(walkLeft[self.walkcount//5],(self.x,self.y) )
            self.walkcount+=1
        elif self.wright:
            self.walkcount+=1
            screen.blit(walkRight[self.walkcount//5],(self.x,self.y) )
        if self.chargecount<160:
            if self.fitu:
                screen.blit(chtous[self.walkcount//5],(self.x,self.y) )
            elif self.fifa:
                screen.blit(chfaraway[self.walkcount//5],(self.x,self.y) )
            elif self.file:
                screen.blit(chLeft[self.walkcount//5],(self.x,self.y) )
            elif self.firi:
                screen.blit(chRight[self.walkcount//5],(self.x,self.y) )
        else:
            if self.fitu:
                screen.blit(firetous[self.walkcount//5],(self.x,self.y) )
            elif self.fifa:
                screen.blit(firefaraway[self.walkcount//5],(self.x,self.y) )
            elif self.file:
                screen.blit(fireLeft[self.walkcount//5],(self.x,self.y) )
            elif self.firi:
               screen.blit(fireRight[self.walkcount//5],(self.x,self.y) )
        
            
        if self.firi or self.file or self.fitu or self.fifa:
            if self.chargecount>=200:
                self.chargecount+=0
            else:
                self.chargecount+=1
                
def bulcheck(index):#не рабочая штука для удаления пули
    if bul[i].x>=width or bul[i].x<=0:
        bul[i].isxist=False
    if bul[i].y>=height or bul[i].y<=0:
        bul[i].isxist=False

def walkall():
    j=0
    while j<krcount:
        if kr[j].walkdir == 1:
            kr[j].x+=kr[j].speedx
            kr[j].y+=kr[j].speedy
        b1=False
        b2=False
        
        
        if (kr[j].y>=height-74 or kr[j].y<=0):
            kr[j].speedy=-kr[j].speedy
            
        if (kr[j].x>=width-50 or kr[j].x<=0):
            kr[j].speedx=-kr[j].speedx
        j+=1
    

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
    if bul[1].isexist:
        bul[1].draw(screen)
    if bul[2].isexist:
        bul[2].draw(screen)
    if bul[3].isexist:
        bul[3].draw(screen)
    if bul[0].isexist:
        bul[0].draw(screen)
    pygame.display.update()
running = True

def hitself():#для проверки
    myhp.hp-=1

#mainloop
i=-1
part=1
man = player(200,100,32,32)
bul = [bullet(man.x,man.y,1),bullet(man.x,man.y,1),bullet(man.x,man.y,1),bullet(man.x,man.y,1)]
enem = []
j=0
kr=[]
krcount=0
enemycount=0
timerforenemy=0
myhp=health(5,2)
something=False
while running:
    i+=1
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
        bul[i].direct=1
        
    elif keys[pygame.K_a] and man.x>man.speed:
        man.x -= man.speed
        man.wleft = True
        man.wright =False
        man.wfaraw=False
        man.wtus=False
        bul[i].direct=3

    elif keys[pygame.K_d] and man.x < width-man.a-man.speed:
        man.x += man.speed
        man.wleft=False
        man.wright=True
        man.wfaraw=False
        man.wtus=False
        bul[i].direct=1

    if keys[pygame.K_s]and keys[pygame.K_w]:
        man.wleft=False
        man.wright = False
        man.wfaraw=False
        man.wtus=True
        bul[i].direct=4
        
    elif keys[pygame.K_w] and man.y>man.speed:
        man.y -= man.speed
        man.wleft=False
        man.wright = False
        man.wfaraw=True
        man.wtus=False
        bul[i].direct=2
        
    elif keys[pygame.K_s]and man.y < height-man.a-man.a-man.speed:
        man.y += man.speed
        man.wleft=False
        man.wright = False
        man.wfaraw=False
        man.wtus=True
        bul[i].direct=4

    b=not(keys[pygame.K_s] or keys[pygame.K_w] or keys[pygame.K_d] or keys[pygame.K_a])
    
    if keys[pygame.K_KP6]:
        man.firi=True
        man.file=False
        man.fitu=False
        man.fifa=False
        bul[i].direct=1
        if b:
            man.wleft=False
            man.wright=True
            man.wfaraw=False
            man.wtus=False
        
    elif keys[pygame.K_KP4]:
        man.firi=False
        man.file=True
        man.fitu=False
        man.fifa=False
        bul[i].direct=3
        if b:
            man.wleft = True
            man.wright =False
            man.wfaraw=False
            man.wtus=False

    elif keys[pygame.K_KP8]:
        man.firi=False
        man.file=False
        man.fitu=False
        man.fifa=True
        bul[i].direct=2
        if b:
            man.wleft=False
            man.wright = False
            man.wfaraw=True
            man.wtus=False
        
    elif keys[pygame.K_KP2]:
        man.firi=False
        man.file=False
        man.fitu=True
        man.fifa=False
        bul[i].direct=4
        if b:
            man.wleft=False
            man.wright = False
            man.wfaraw=False
            man.wtus=True

    else:
        man.firi=False
        man.file=False
        man.fitu=False
        man.fifa=False
    #key input end
    if keys[pygame.K_KP2] or keys[pygame.K_KP8] or keys[pygame.K_KP4] or keys[pygame.K_KP6]:
        if man.chargecount>=160 and keys[pygame.K_KP5]:#input for shoot
            bul[i].isexist=True
            man.chargecount=0
            bul[i].__init__(man.x,man.y,bul[i].direct)
            bul[i].isexist=True
    j=3
    if keys[pygame.K_KP9]:#input to hurt myself
        if not (something):
            hitself()
            something=True
        
    else:
        something = False
    while j>=0:
        if bul[j].direction==1:
            bul[j].x+=bul[j].speed
        elif bul[j].direction==2:
            bul[j].y-=bul[j].speed
        elif bul[j].direction==3:
            bul[j].x-=bul[j].speed
        elif bul[j].direction==4:
            bul[j].y+=bul[j].speed
        bulcheck(j)
        j-=1
    timerforenemy+=1
    if timerforenemy>=300:#enemy spawn timer
            timerforenemy=0#enemy spawn timer = 0
            krcount+=1#колличество врагов + 1
            kr.append(krest(r.randint(0,width-50),r.randint(0,height-74),1))#враг + 1 в список
    pygame.display.flip()
    screen.blit(bg,(0,0))
    redrawGameWindow()
    walkall()
    if myhp.hp<=0:
        running=False
