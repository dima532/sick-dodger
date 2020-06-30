import sys,pygame
import time
class textur():
    def load(self):
        self.walkRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_0/7.png'))]

        self.walkLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_0/7.png'))]

        self.walkfaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

        self.walktous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_0/7.png'))]

        self.chRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_1/7.png'))]

        self.chLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_1/7.png'))]

        self.chfaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

        self.chtous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_1/7.png'))]

        self.fireRight=[pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/r/ch_2/7.png'))]

        self.fireLeft=[pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/l/ch_2/7.png'))]

        self.firefaraway=[pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna1/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna3/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna4/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna5/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna6/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/b/volna7/1.png'))]

        self.firetous=[ pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/4.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/5.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/6.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/f/ch_2/7.png'))]

        self.bull=[pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/Bullet/4.png'))]

        self.hp=[pygame.transform.scale2x(pygame.image.load('sphere drone/battery/3.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/battery/2.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/battery/1.png')),
        pygame.transform.scale2x(pygame.image.load('sphere drone/battery/0.png'))]

        self.bg= pygame.transform.scale2x(pygame.image.load('sphere drone/fone.png'))

        self.kres0=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/2.png')),
          pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 0/4.png')),]

        self.kres1=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/2.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 1/4.png')),]

        self.kres2=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/2.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 2/4.png')),]

        self.kres3=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/2.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 3/4.png')),]

        self.kres4=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/2.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 4/4.png')),]

        self.kres5=[pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/1.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/2.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/3.png')),
           pygame.transform.scale2x(pygame.image.load('sphere drone/enemy/X/charge 5/4.png')),]
