import sys,pygame
import time

class rect():
    def __init__(self,x,y,a,b,c,d):
        self.x=x
        self.y=y
        self.bot=a
        self.right=b
        self.vert=c
        self.gor=d
        self.leftcol=((self.right+self.x)/2)-self.gor
        self.rightcol=((self.right+self.x)/2)+self.gor
        self.botcol=self.bot-self.vert
        self.topcol=self.y
